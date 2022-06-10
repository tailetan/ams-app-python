import sys

from lib.wtforms.fields.core import StringField
from lib.wtforms.form import Form

print(sys.getrecursionlimit())
reload(sys)
sys.setdefaultencoding('utf8')
from lib.wtforms import *
import datetime

from lib.wtforms import validators


class CreateUserForm(Form):
    first_name = StringField('First Name', validators=[
        validators.input_required()])
    last_name = StringField('Last Name', validators=[
        validators.input_required()])
    date_of_birth = StringField('Date Of Birth', validators=[
        validators.input_required()])
    gender = StringField('Gender', validators=[
        validators.input_required()])
    joined_date = StringField('Join Date', validators=[
        validators.input_required()])
    role = StringField('Role', validators=[
        validators.input_required()])
    location = StringField('Location', validators=[
        validators.input_required()])

    def validate_date_of_birth(form, field):
        start_date = datetime.datetime.strptime(
            str(field.data), '%Y-%m-%d').date()
        end_date = datetime.datetime.strptime(
            str(datetime.date.today()), '%Y-%m-%d').date()
        day_between_dates = ((end_date.year - start_date.year) -
                             ((end_date.month, end_date.day) < (start_date.month, start_date.day)))
        if day_between_dates < 18:
            raise ValidationError(
                "User must be 18 or older")

    def format_date_of_birth(form, date):
        date = datetime.datetime.strptime(
            str(date.data), '%Y-%m-%d').date()
        return date

    def day_between_dates(self, start_date, end_date):
        day_between_dates = ((end_date.year - start_date.year) -
                             ((end_date.month, end_date.day) < (start_date.month, start_date.day)))
        return day_between_dates

    def validate_joined_date(form, field):
        joined_date = datetime.datetime.strptime(
            str(field.data), '%Y-%m-%d').date()
        if joined_date.weekday() >= 5 or form.day_between_dates(form.format_date_of_birth(form.date_of_birth),
                                                                joined_date) < 18:
            raise ValidationError(
                "User must join on weekdays and must be greater or equal 18 years old when joining the company")

    def validate_location(form, field):

        if field.data not in ('Ho Chi Minh', 'Ha Noi', 'Da Nang'):
            raise ValidationError(
                "Location must be Ho Chi Minh, Da Nang or Ha Noi")
            # form.response.out.write("Location must be Ho Chi Minh, Da Nang or Ha Noi")

