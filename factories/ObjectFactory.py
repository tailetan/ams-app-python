from ClassList.InvokerClassList import INVOKER_CLASS_LIST
from ClassList.UserClassList import USER_CLASS_LIST
from ClassList.CategoryClassList import CATEGORY_CLASS_LIST
from factories.ClassList.CommandClassList import COMMAND_CLASS_LIST
from factories.ClassList.FilterClassList import FILTER_CLASS_LIST
from factories.ClassList.FormClassList import FORM_CLASS_LIST
# from factories.ClassList.PaginationClassList import PAGINATION_CLASS_LIST
from factories.ClassList.SortClassList import SORT_CLASS_LIST


class ObjectFactory(object):
    @staticmethod
    def create_invoker_object(object_name):
        return INVOKER_CLASS_LIST[object_name]()

    @staticmethod
    def create_command_object(object_name, **kwargs):
        return COMMAND_CLASS_LIST[object_name](**kwargs)

    @staticmethod
    def create_form_object(object_name, *args):
        return FORM_CLASS_LIST[object_name](*args)

    @staticmethod
    def create_filter_object(object_name, **kwargs):
        return FILTER_CLASS_LIST[object_name](**kwargs)

    @staticmethod
    def create_sort_object(object_name, **kwargs):
        return SORT_CLASS_LIST[object_name](**kwargs)

    @staticmethod
    def create_user_object(object_name, **kwargs):
        return USER_CLASS_LIST[object_name](**kwargs)

    @staticmethod
    def create_category_object(object_name, **kwargs):
        return CATEGORY_CLASS_LIST[object_name](**kwargs)

    # @staticmethod
    # def create_pagination_object(object_name):
    #     return PAGINATION_CLASS_LIST[object_name]()

