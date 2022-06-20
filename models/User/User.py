import hashlib
import uuid
import sys

# from lib.wtforms.ext.appengine import ndb
# from models.User.Create.CreateUsername import CreateUsername
# from wtforms.ext.appengine import db

reload(sys)
sys.setdefaultencoding('utf8')

from models.BaseModel import *
from models.User.Create.CreateStaffCode import CreateStaffCode as ctc

from models.BaseModel import BaseModel as bm
import datetime


class User(BaseModel):
    first_name = ndb.StringProperty()
    last_name = ndb.StringProperty()
    full_name = ndb.StringProperty()
    staff_code = ndb.StringProperty()
    date_of_birth = ndb.StringProperty()
    gender = ndb.StringProperty()
    role = ndb.StringProperty()
    joined_date = ndb.StringProperty()
    password = ndb.StringProperty()
    username = ndb.StringProperty()
    location = ndb.StringProperty()

    def count_user(self):
        result = self.count_entities(User())
        return result

    def get_list_model(self, **kwargs):
        from factories.ObjectFactory import ObjectFactory
        object = ObjectFactory.create_user_object(
            'GetUser',
            user_model=User,
            invoker=kwargs['invoker'],
            object_factory=ObjectFactory,
            location_params=kwargs['location_params'],
            role_params=kwargs['role_params'],
            sort_params=kwargs['sort_params'],
            sort_direction=kwargs['sort_direction'],
            response_out_write=kwargs['response_out_write']
        )
        result = object.get_users()
        kwargs['response_out_write'](result)

    def create_model(self, form):
        from factories.ObjectFactory import ObjectFactory
        obj = ObjectFactory.create_user_object(
            'CreateUser',
            staff_code=self.staff_code,
            first_name=self.first_name,
            last_name=self.last_name,
            date_of_birth=self.date_of_birth,
            joined_date=self.joined_date,
            location=self.location,
            role=self.role,
            count_user=self.count_user()
        )
        obj.create_user(User(), form)

    def serializable(self):
        return {
            "id": self.id.__str__(),
            "time_created": self.time_created.strftime("%Y-%m-%d %H:%M:%S"),
            "time_last_modified": self.time_last_modified.strftime("%Y-%m-%d %H:%M:%S"),
            "first_name": self.first_name,
            "last_name": self.last_name,
            "full_name": self.full_name,
            "username": self.username,
            "joined_date": self.joined_date,
            "password": self.password,
            "staff_code": self.gender,
            "location": self.gender,

            "date_of_birth": self.date_of_birth
        }
