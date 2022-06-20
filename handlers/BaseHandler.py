import json
import datetime

import webapp2
import sys

sys.path.insert(1, '/Users/tantaile/Desktop/Python/ams-app/google-cloud-sdk/platform/google_appengine')
sys.path.insert(1,
                '/Users/tantaile/Desktop/Python/ams-app/google-cloud-sdk/platform/google_appengine/lib/yaml-3.10/yaml')
if 'google' in sys.modules:
    del sys.modules['google']


from google.appengine.ext import db
# from webapp2_extras import json
from util.Errors import BadRequestException


class BaseHandler(webapp2.RequestHandler):
    def guestbook_key(self, guestbook_name=None):
        """Constructs a datastore key for a Guestbook entity with guestbook_name."""

    def get_params(self):
        try:
            if self.request.body:
                print(json.decode(self.request.body))
                return json.decode(self.request.body)
            else:
                params = self.request.params

                out = {}
                for key in params.keys():
                    out[key] = params[key]

                return out

        except Exception as e:
            e.message = "Invalid Payload. Please check your JSON."
            raise e
            return None

    def assert_params(self, params, fields):
        for field in fields:
            if not params.get(field):
                e = BadRequestException()
                e.message = "Missing '%s' field" % (field)
                raise e

    def respond(self, a={}):

        # try:
        #     db.close()
        # except Exception as e:
        #     print e

        if self.response.body == "":
            self.response.write(json.dumps(a, separators=(',', ':')))

    @staticmethod
    def tuple_to_json(arg):
        req_dic = {}
        for key, value in arg.items():
            # checking for any nested dictionary
            l = key.split(".")
            # if nested dictionary is present
            if len(l) > 1:
                i = l[0]
                j = l[1]
                if req_dic.get(i) is None:
                    req_dic[i] = {}
                    req_dic[i][j] = []
                    req_dic[i][j].append(value)
                else:
                    if req_dic[i].get(j) is None:
                        req_dic[i][j] = []
                        req_dic[i][j].append(value)
                    else:
                        req_dic[i][j].append(value)

            else:  # if single dictionary is there
                if req_dic.get(l[0]) is None:
                    req_dic[l[0]] = value
                else:
                    req_dic[l[0]] = value
        return arg

    def gql_json_parser(self, query_obj):
        result = []
        for entry in query_obj:
            result.append(dict([(p, unicode(getattr(entry, p))) for p in entry.properties()]))
        return result

    def get_filter(self, *args):
        filters = []
        for FILTER in args:
            filter_ = self.request.GET.get(FILTER).split(',')
            filters.append([str(i) for i in filter_])
        return filters

    def return_users(self, filter_name, li_u_removed):
        list_filter = []
        for i in li_u_removed:
            sql = "SELECT * From User WHERE " + filter_name + " = :1"
            q = db.GqlQuery(sql, i)
            list_filter += q

        json_query_data = self.gql_json_parser(list_filter)
        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(json.dumps(json_query_data))

    def return_json(self, arg):
        req_dic = {}
        for key, value in arg:
            # checking for any nested dictionary
            l = key.split(".")
            # if nested dictionary is present
            if len(l) > 1:
                i = l[0]
                j = l[1]
                if req_dic.get(i) is None:
                    req_dic[i] = {}
                    req_dic[i][j] = []
                    req_dic[i][j].append(value)
                else:
                    if req_dic[i].get(j) is None:
                        req_dic[i][j] = []
                        req_dic[i][j].append(value)
                    else:
                        req_dic[i][j].append(value)

            else:  # if single dictionary is there
                if req_dic.get(l[0]) is None:
                    req_dic[l[0]] = value
                else:
                    req_dic[l[0]] = value
        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(json.dumps(req_dic))

    def update_time_last_modified(self):
        if hasattr(self, "time_last_modified"):
            setattr(self, "time_last_modified", datetime.datetime.now())

    def set_values(self, values, variables):

        for var in variables:
            if var in values:
                if hasattr(self, var) and var != "password_hash":
                    if var == "id" or var == "time_created":
                        continue

                    if getattr(self, var) != values[var]:
                        setattr(self, var, values[var])
                        self.update_time_last_modified()

                elif var == "password":
                    # self.set_password(values[var])
                    self.update_time_last_modified()

                else:
                    e = BadRequestException()
                    e.message = "'%s' is not an acceptable value" % (var)