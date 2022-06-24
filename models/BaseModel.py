import uuid
from time import mktime
import datetime
import json

# import sys
# #
# sys.path.insert(1, '/Users/tantaile/Desktop/Python/ams-app/google-cloud-sdk/platform/google_appengine')
# sys.path.insert(1, '/Users/tantaile/Desktop/Python/ams-app/google-cloud-sdk/platform/google_appengine/lib/yaml-3.10/yaml')
# if 'google' in sys.modules:
#     del sys.modules['google']

from google.appengine.ext import ndb

# from google.appengine.ext import db
from lib.peewee import UUIDField


class BaseModel(ndb.Model):
    # id = uuid.uuid4().hex(primary_key=True)
    id = UUIDField(primary_key=True)
    time_created = ndb.DateTimeProperty(auto_now_add=True)
    time_last_modified = ndb.DateTimeProperty(auto_now=True)

    @staticmethod
    def to_timestamp(self, date):
        return mktime(date.timetuple())

    @staticmethod
    def from_timestamp(self, time):
        return datetime.datetime.fromtimestamp(int(time))

    def update_time_last_modified(self):
        if hasattr(self, "time_last_modified"):
            setattr(self, "time_last_modified", datetime.datetime.now())

    def validate_datetime_format(date_text):
        try:
            datetime.datetime.strptime(date_text, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Incorrect data format, should be YYYY-MM-DD")

    @staticmethod
    def count_entities(self, model):
        result = model.query().count()
        return result

    @staticmethod
    def gql_json_parser(self, query_obj):
        result = []
        for entry in query_obj:
            result.append(dict([(p, unicode(getattr(entry, p))) for p in entry._properties()]))
        return result

    # @staticmethod
    def json_parser_get_list(self, **kwargs):
        return json.dumps({
            'total': kwargs['total'],
            'per_page': kwargs['per_page'],
            'current_page': kwargs['current_page'],
            'last_page': kwargs['last_page'],
            'from': kwargs['from_result'],
            'to': kwargs['to_result'],
            'first_page_url': kwargs['first_page_url'],
            'last_page_url': kwargs['last_page_url'],
            'prev_page_url': kwargs['prev_page_url'],
            'next_page_url': kwargs['next_page_url'],
            'data': [a.to_dict() for a in kwargs['query_obj']]},
            indent=4, sort_keys=True, default=str)
