import sys

from lib.wtforms import validators
from lib.wtforms.fields.core import StringField
from lib.wtforms.form import Form

reload(sys)
sys.setdefaultencoding('utf8')
from lib.wtforms import *
import datetime


class CreateAssetForm(Form):
    asset_name = StringField('Name', validators=[
                            validators.input_required()])
    category = StringField('Category', validators=[
                            validators.input_required()])
    asset_specification = StringField('Specification', validators=[
                            validators.input_required()])
    asset_installed_date = StringField('Installed date', validators=[
                            validators.input_required()])
    # state = StringField('State', validators=[
    #     validators.input_required()])
