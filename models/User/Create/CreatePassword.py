from datetime import datetime

from lib.webapp2_extras.security import generate_password_hash


class CreatePassword():
    def __init__(self, **kwargs):
        self.attributes = kwargs

    def format_date_of_birth(self):
        d = datetime.strptime(
            str(self.attributes['date_of_birth']), '%Y-%m-%d').date()
        return d.strftime('%d%m%Y')

    def generate_password(self):
        pw = (
            self.attributes['username'] + '@' +
            self.format_date_of_birth()
        )
        return generate_password_hash(pw)
