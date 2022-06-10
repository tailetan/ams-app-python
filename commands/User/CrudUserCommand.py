from commands.CRUDCommand import *


class CrudUserCommand(CRUDCommand):
    def __init__(self, **kwargs):
        self._attributes = kwargs

    def get_list(self):
        self._attributes['user'].get_list_model(
            cursor=self._attributes['cursor'],
            location_params=self._attributes['location_params'],
            invoker=self._attributes['invoker'],
            role_params=self._attributes['role_params'],
            sort_params=self._attributes['sort_params'],
            sort_direction=self._attributes['sort_direction'],
            response_out_write=self._attributes['response_out_write']
        )

    def create(self):
        self._attributes['user'].create_model(self._attributes['form'])
