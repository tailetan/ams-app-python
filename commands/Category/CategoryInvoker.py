class CategoryInvoker:
    def __init__(self):
        self._commands = {}

    def register(self, command_name, command):
        self._commands[command_name] = command

    def execute(self, command_name):
        if command_name in self._commands.keys():
            if command_name == 'get_list_category':
                self._commands[command_name].get_list()
            if command_name == 'create_category':
                self._commands[command_name].create_category()
        else:
            print('Command [{command_name}] not recognised')
