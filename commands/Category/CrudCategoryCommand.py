from commands.CRUDCommand import *


class CrudUserCommand(CRUDCommand):
    def __init__(self, **kwargs):
        self._attributes = kwargs


    def create_category(self):
        self._attributes['category'].create_model(self._attributes['form'])
