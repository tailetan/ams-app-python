from commands.CRUDCommand import *


class CrudUserCommand(CRUDCommand):
    def __init__(self, **kwargs):
        self._attributes = kwargs

    def get_list_category(self):
        self._attributes['category'].get_list_model(
            invoker=self._attributes['invoker'],
            response_out_write=self._attributes['response_out_write']
        )

    def create_category(self):
        self._attributes['category'].create_model(self._attributes['form'])
