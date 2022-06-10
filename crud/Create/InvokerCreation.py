class InvokerCreation:
    def __init__(self):
        self._crud = {}

    def register(self, crud_name, crud):
        self._crud[crud_name] = crud

    def execute(self, crud_name):
        if crud_name in self._crud.keys():
            self._crud[crud_name].create()
        else:
            print('crud [{crud_name}] not recognised')
