class CreateFullName:
    def __init__(self, **kwargs):
        self.attributes = kwargs

    def generate_full_name(self):
        return (
            self.attributes['user_model'].first_name + ' ' +
            self.attributes['user_model'].last_name
        )
