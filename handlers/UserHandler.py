from factories.ObjectFactory import ObjectFactory
from models.User.User import *
from forms.User.CreateUserForm import *

# from google.appengine.api import user
sys.path.insert(1, '/Users/tantaile/Desktop/Python/ams-app/google-cloud-sdk/platform/google_appengine')
sys.path.insert(1,
                '/Users/tantaile/Desktop/Python/ams-app/google-cloud-sdk/platform/google_appengine/lib/yaml-3.10/yaml')
if 'google' in sys.modules:
    del sys.modules['google']
from google.appengine.ext import db
from BaseHandler import *


class UserHandler(BaseHandler):
    invoker = ObjectFactory.create_invoker_object('UserInvoker')
    user_object = ObjectFactory.create_user_object('User')
    """

    Create a User

    """

    # def __init__(self, request=None, response=None):
    #     super(UserHandler, self).__init__(request, response)
    #     # self.query = None

    def post(self):
        form_object = ObjectFactory.create_form_object(
            'CreateUserForm',
            self.request.POST,
            self.user_object
        )
        if self.request.POST and form_object.validate():
            form_object.populate_obj(self.user_object)
            command_create_object = ObjectFactory.create_command_object(
                'CrudUserCommand',
                user=self.user_object,
                form=form_object
            )
            self.invoker.register('create', command_create_object)
            self.invoker.execute('create')
        self.return_json(self.request.POST.items())






    def get(self, user_id=None):

        # users = User.all()
        if self.request.GET.get('user_id'):
            q = db.GqlQuery("SELECT * From User WHERE id = :1", user_id)
            json_query_data = self.gql_json_parser(q)
            self.response.headers['Content-Type'] = 'application/json'
            self.response.out.write(json.dumps(json_query_data))
        else:

            command_get_list_object = ObjectFactory.create_command_object(
                'CrudUserCommand',
                user=self.user_object,
                invoker=self.invoker,
                location_params=str(
                    self.request.GET.get('location')).split(','),
                role_params=str(
                    self.request.GET.get('role')).split(','),
                sort_params=self.request.GET.get('sort_params'),
                sort_direction=self.request.GET.get('sort_direction'),
                cursor=ndb.Cursor(urlsafe=self.request.get('cursor', default_value=None)),
                response_out_write=self.response.out.write

            )
            self.invoker.register('get_list', command_get_list_object)
            self.invoker.execute('get_list')


        #     if self.request.GET.get('location') and not self.request.GET.get('role'):
        #         self.return_users('location', self.get_filter('location')[0])
        #
        #     elif self.request.GET.get('role') and not self.request.GET.get('location'):
        #         self.return_users('role', self.get_filter('role')[0])
        #
        #     elif self.request.GET.get('role') and self.request.GET.get('location'):
        #         filter_location = self.request.GET.get('location').split(',')
        #         filter_role = self.request.GET.get('role').split(',')
        #         li_u_removed_location = [str(i) for i in filter_location]
        #         li_u_removed_role = [str(i) for i in filter_role]
        #         list_filter = []
        #         q = db.GqlQuery("SELECT * From User WHERE location IN :1 AND role IN :2 ORDER BY staff_code ASC", li_u_removed_location,li_u_removed_role)
        #         list_filter += q
        #         json_query_data = self.gql_json_parser(list_filter)
        #         self.response.headers['Content-Type'] = 'application/json'
        #         self.response.out.write(json.dumps(json_query_data))
        # if self.request.GET.get('sort'):
        #     filter_role = self.request.GET.get('sort').split(',')
        #     li_u_removed_sort = [str(i) for i in filter_role]
        #     list_sort = []
        #     q = db.GqlQuery("SELECT * From User ORDER BY staff_code ASC",
        #                     li_u_removed_location, li_u_removed_role)

    # def get(self, user_id=None):
    #
    #     users = User.all()
    #     users.order('is_admin')
    #     if user_id:
    #         q = db.GqlQuery("SELECT * From User WHERE id = :1", user_id)
    #         # users.filter("first_name =", "Tai")
    #         # print users
    #         json_query_data = gql_json_parser(q)
    #         self.response.headers['Content-Type'] = 'application/json'
    #         self.response.out.write(json.dumps(json_query_data))
    #     else:
    #         if self.request.GET.get('location'):
    #             users.filter("location =", location)
    #             json_query_data = gql_json_parser(users)
    #             self.response.headers['Content-Type'] = 'application/json'
    #             self.response.out.write(json.dumps(json_query_data))

    # @staticmethod
    # def getById(self):
    # user = User.get(User.id == self.user_id)
    # self.response.headers['Content-Type'] = 'application/json'
    # self.response.out.write(json.dumps(user))
    # q = db.GqlQuery("SELECT * From User WHERE first_name = :1", "Hao")
    # users.filter("first_name =", "Tai")
    # print users
    # json_query_data = gql_json_parser(q)
    # self.response.headers['Content-Type'] = 'application/json'
    # self.response.out.write("json.dumps(json_query_data)")
    # def put(self):

    #
    #     try:
    #
    #         # get post body
    #
    #         post = self.get_params()
    #
    #         # verify token, get active org
    #
    #         user = User().from_token(self.token())
    #
    #         # update new fields
    #
    #         user.set_values(
    #             post, ["name", "email", "username", "password", "bio"])
    #
    #         # save the admin
    #
    #         user.save()
    #
    #         self.respond(user.serializable())
    #
    #     except Exception as e:
    #
    #         self.error(e)
    #         return
    #
    # def get(self, user_id=None, search=None):
    #     try:
    #         user = User()
    #         if user_id:  # get single user
    #             # get the user
    #             user = User.get(User.id == user_id)
    #             # respond with single user
    #             self.respond(user.serializable())
    #         else:  # searching for users
    #             # get the params
    #             get = self.get_params()
    #             # get the admins
    #             get_users = User.matching_params(
    #                 get, ["full_name", "date_of_birth", "username", ])
    #             # respond with the admins
    #             self.respond(get_users)
    #     except Exception as e:
    #         self.error(e)
    #         return
    #
    # def delete(self, admin_id):
    #
    #     try:
    #
    #         user = User().from_token(self.token())
    #
    #         user.delete_instance()
    #
    #         self.respond()
    #
    #     except Exception as e:
    #         self.error(e)
    #         return
