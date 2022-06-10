from crud.CRUD import CRUD


class CreateUserCommand(CRUD):
    def __init__(self, receiver, form, **kwargs):
        self._receiver = receiver
        self._form = form
        self.attributes = kwargs

    def get_list(self):
        self.attributes['user'].get_list_model(self.attributes['response_out_write'])

    def create(self):
        self._receiver.create_user(self._form)
