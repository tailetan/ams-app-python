from decorators.LocationFilter import LocationFilter
from decorators.RoleFilterDecorator import RoleFilterDecorator
from strategies.Filter.FilterLocationRequest import FilterLocationRequest
from strategies.Filter.FilterRoleRequest import FilterRoleRequest
from strategies.Filter.FilteredList import FilteredList


FILTER_CLASS_LIST = {
    'LocationFilter': LocationFilter,
    'RoleFilterDecorator': RoleFilterDecorator,
    'FilteredList': FilteredList,
    'FilterLocationRequest': FilterLocationRequest,
    'FilterRoleRequest': FilterRoleRequest
}