import webapp2
from test_base import BaseTestCase
import main
import models


class UserHandler(webapp2.RequestHandler):
    # def post(self, search=None):
    #     user = User()
    #     form = UserForm(self.request.POST, user)
    #     if self.request.POST and form.validate():
    #         form.populate_obj(user)
    #         user.format_input()
    #         user.generate_staff_code()
    #         user.create_username()
    #         user.create_hash_password()
    #         user.create_fullname()
    #         user.save()

    def post(self, **kwargs):
        self.response.status_code = 200


app = webapp2.WSGIApplication([
    webapp2.Route('/', UserHandler, name='user'),

], debug=False)


class TestHandler(BaseTestCase):
    def tearDown(self):
        super(TestHandler, self).tearDown()
        app.error_handlers = {}

    def test_200(self):
        request = webapp2.Request.blank('/user')
        request.method = 'POST'
        rsp = request.get_response(app)

        self.assertEqual(rsp.status_int, 200)
        # self.assertEqual(rsp.body, b'home sweet home
    #
    # def test_404(self):
    #     req = webapp2.Request.blank('/nowhere')
    #     rsp = req.get_response(app)
    #     self.assertEqual(rsp.status_int, 404)

    # def test_create(self):
    #     request = webapp2.Request.blank('/')
    #     request.method = 'POST'
    #     response = request.get_response(main.application)
    #
    #     # Let's check if the response is correct.
    #     self.assertEqual(response.status_int, 200)
