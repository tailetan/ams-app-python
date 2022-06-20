import sys

# from lib.wtforms.ext.appengine import ndb
from models.Category.Create.CreatePrefix import CreatePrefix
# from wtforms.ext.appengine import db

reload(sys)
sys.setdefaultencoding('utf8')

from models.BaseModel import *


class Category(BaseModel):
    category_name = ndb.StringProperty()
    category_prefix = ndb.StringProperty()
    # assets = ndb.KeyProperty()

    def create_prefix(self):
        self.category_prefix = CreatePrefix.get_prefix(self.category_name)
        return self.category_prefix

    def create_model(self, form):
        from factories.ObjectFactory import ObjectFactory
        obj = ObjectFactory.create_category_object(
            'CreateCategory',
            category_name=self.category_name,
            category_prefix=self.category_prefix
        )
        obj.create_user(Category(), form)
    # def serializable(self):
    #     return {
    #         "time_created": self.time_created,
    #         "time_last_modified": self.time_last_modified,
    #         "category_name": self.category_name,
    #
    #     }

