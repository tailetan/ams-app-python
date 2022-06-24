from models.User.Create.CreateFullName import CreateFullName
from models.User.Create.CreatePassword import CreatePassword
from models.User.Create.CreateStaffCode import CreateStaffCode
from models.User.Create.CreateUser import CreateUser
from models.User.Create.CreateUsername import CreateUsername
from models.User.GetUser.GetUsersByLocationFilter import GetUserByLocationFilter
from models.User.GetUser.GetUsersByRoleFilter import GetUserByRoleFilter
from models.User.User import User
from models.User.GetUser.GetUsers import GetUsers
from models.User.GetUser.GetUsersFilterDecorator import GetUserFilterDecorator
from models.User.UserPagination.UserPagination import UserPagination
from models.User.UserPagination.UserParamsUrl import UserParamsUrl

USER_CLASS_LIST = {
    'User': User,
    'GetUsers': GetUsers,
    # 'GetAllUser': GetAllUser,
    'GetUserByLocationFilter': GetUserByLocationFilter,
    'GetUserByRoleFilter': GetUserByRoleFilter,
    'GetUserFilterDecorator': GetUserFilterDecorator,
    'CreateUser': CreateUser,
    'CreateUsername': CreateUsername,
    'CreatePassword': CreatePassword,
    'CreateStaffCode': CreateStaffCode,
    'CreateFullName': CreateFullName,
    'UserPagination': UserPagination,
    'UserParamsUrl': UserParamsUrl
}