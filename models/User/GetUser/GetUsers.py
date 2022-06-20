import json
from models.BaseModel import *


class GetUser(BaseModel):
    def __init__(self, **kwargs):
        self.attributes = kwargs

    def get_all_user(self):
        query = self.attributes['user_model'].all()
        return query

    def get_user_location_role_filter_list(self, query):
        obj = self.attributes['object_factory'].create_user_object(
            'GetUserFilterDecorator',
            object_factory=self.attributes['object_factory'],
            query=query,
            model=self.attributes['user_model'],
            location_params=self.attributes['location_params'],
            role_params=self.attributes['role_params']
        )
        return obj.get_user_location_role_filter_list()

    def get_user_location_filter_list(self, query):
        obj = self.attributes['object_factory'].create_user_object(
            'GetUserByLocationFilter',
            object_factory=self.attributes['object_factory'],
            model=self.attributes['user_model'],
            query=query,
            location_params=self.attributes['location_params']
        )
        return obj.get_user_by_location_filter()

    def get_user_role_filter_list(self, query):
        obj = self.attributes['object_factory'].create_user_object(
            'GetUserByRoleFilter',
            object_factory=self.attributes['object_factory'],
            model=self.attributes['user_model'],
            query=query,
            role_params=self.attributes['role_params']
        )
        return obj.get_user_by_role_filter()

    def get_users(self):
        query = self.attributes['user_model'].query()

        if self.attributes['location_params'][0] == 'None':
            result = self.get_user_role_filter_list(query)
        elif self.attributes['role_params'][0] == 'None':
            result = self.get_user_location_filter_list(query)
        else:
            result = self.get_user_location_role_filter_list(query)

        sort_object = self.attributes['object_factory'].create_sort_object(
            self.attributes['sort_params'],
            model=self.attributes['user_model'],
            query=result,
            sort_direction=self.attributes['sort_direction']
        )

        result = self.attributes['object_factory'].create_sort_object(
            'SortedList'
        ).sort_request(sort_object)

        #
        # return result
        # return json.dumps(a for a in result)
        def set_default(obj):
            if isinstance(obj, set):
                return list(obj)
            raise TypeError

        return json.dumps([a.to_dict() for a in result], indent=4, sort_keys=True, default=str)
        # return json.dumps('data': [a.to_dict() for a in result])
