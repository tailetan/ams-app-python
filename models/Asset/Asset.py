import sys

# from lib.wtforms.ext.appengine import ndb
from models.Category.Category import Category
# from wtforms.ext.appengine import ndb
from models.BaseModel import *

reload(sys)
sys.setdefaultencoding('utf8')


class Asset(BaseModel):
    asset_code = ndb.StringProperty()
    asset_name = ndb.StringProperty()
    asset_specification = ndb.StringProperty()
    asset_installed_date = ndb.StringProperty()
    # category = db.ReferenceProperty(Category)

    # def create_prefix(self):
    #     self.category_prefix = CreatePrefix.get_prefix(self.category_name)
    #     return self.category_prefix

    # def serializable(self):
    #     return {
    #         "time_created": self.time_created,
    #         "time_last_modified": self.time_last_modified,
    #         "category_name": self.category_name,
    #
    #     }
