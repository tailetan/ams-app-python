class UserParamsUrl():
    def __init__(self, **kwargs):
        self.attributes = kwargs

    def create_params_url(self):
        params_url = {
            'location': ','.join(self.attributes['location_params']),
            'role': ','.join(self.attributes['role_params'])
        }

        return params_url
