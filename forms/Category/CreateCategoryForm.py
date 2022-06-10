import sys

from lib.wtforms import validators
from lib.wtforms.fields.core import StringField
from lib.wtforms.form import Form

reload(sys)
sys.setdefaultencoding('utf8')
from lib.wtforms import *


class CreateCategoryForm(Form):
    category_name = StringField('Category Name', validators=[
        validators.input_required()])
