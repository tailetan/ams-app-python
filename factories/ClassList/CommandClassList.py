from commands.User.CrudUserCommand import CrudUserCommand
from commands.User.UserPaginationCommand import UserPaginationCommand



COMMAND_CLASS_LIST = {
    'CrudUserCommand': CrudUserCommand,
    'CrudCategoryCommand': CrudUserCommand,
    'UserPaginationCommand': UserPaginationCommand,

}