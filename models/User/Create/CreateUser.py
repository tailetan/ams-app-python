from models.BaseModel import *


class CreateUser():
    def __init__(self, **kwargs):
        self.attributes = kwargs

    def create_staff_code(self, object_factory):
        serial_number = self.attributes['count_user'] + 1
        object = object_factory.create_user_object(
            'CreateStaffCode',
            serial_number=serial_number
        )
        return object.generate_staffcode()

    def create_username(self, object_factory, user_model):
        object = object_factory.create_user_object(
            'CreateUsername',
            user_model=user_model
        )
        return object.generate_username()

    def create_password(self, object_factory, username):
        object = object_factory.create_user_object(
            'CreatePassword',
            username=username,
            date_of_birth=self.attributes['date_of_birth']
        )
        return object.generate_password()

    def create_full_name(self, object_factory, user_model):
        object = object_factory.create_user_object(
            'CreateFullName',
            user_model=user_model
        )
        return object.generate_full_name()

    def format_input(self, user_model):
        user_model.first_name = self.attributes['first_name'].title()
        user_model.last_name = self.attributes['last_name'].title()

    def create_user(self, user_model, form):
        from factories.ObjectFactory import ObjectFactory
        user = user_model
        form.populate_obj(user)
        self.format_input(user)
        user.staff_code = self.create_staff_code(ObjectFactory)
        user.username = self.create_username(ObjectFactory, user)
        user.password = self.create_password(ObjectFactory, user.username)
        user.full_name = self.create_full_name(ObjectFactory, user)
        user.put()
