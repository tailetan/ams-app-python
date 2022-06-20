from urlparse import urlparse, parse_qs

from factories.ObjectFactory import ObjectFactory
from google.appengine.api.search import search
from models.User.User import *
from forms.User.CreateUserForm import *

# from google.appengine.api import user
sys.path.insert(1, '/Users/tantaile/Desktop/Python/ams-app/google-cloud-sdk/platform/google_appengine')
sys.path.insert(1,
                '/Users/tantaile/Desktop/Python/ams-app/google-cloud-sdk/platform/google_appengine/lib/yaml-3.10/yaml')
if 'google' in sys.modules:
    del sys.modules['google']
from google.appengine.ext import ndb
from BaseHandler import *

_INDEX_NAME = 'greeting'


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

        if user_id:
            u = User.get_by_id(int(user_id))
            self.respond(u.serializable() if u is not None else "User not found")
            # self.response.out.write(u if u is not None else "No user was found")
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


    # def put(self):
    #
    #     try:
    #         # get post body
    #         post = self.get_params()
    #         # verify token, get active org
    #         user = User().from_token(self.token())
    #         # update new fields
    #         user.set_values(
    #             post, ["name", "email", "username", "password", "bio"])
    #         # save the admin
    #         user.save()
    #         self.respond(user.serializable())
    #     except Exception as e:
    #
    #         self.error(e)
    #         return
    #
