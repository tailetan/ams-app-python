class CreateStaffCode():
    def __init__(self, **kwargs):
        self.attributes = kwargs

    prefix = 'SD'

    def generate_staffcode(self):
        return self.prefix + str(self.attributes['serial_number']).rjust(4, '0')
