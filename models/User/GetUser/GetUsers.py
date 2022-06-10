import json
from models.BaseModel import *


class GetUser(BaseModel):
    def __init__(self, **kwargs):
        self.attributes = kwargs

    def get_all_user(self, object_factory):
        object = object_factory(
            'GetAllUser',
            user_model=self.attributes['user_model']
        )
        return object.get_all_user()

    def get_user_location_role_filter_list(self, query):
        object = self.attributes['object_factory'].create_user_object(
            'GetUserFilterDecorator',
            object_factory=self.attributes['object_factory'],
            query=query,
            user_model=self.attributes['user_model'],
            location_params=self.attributes['location_params'],
            role_params=self.attributes['role_params']
        )
        return object.get_user_location_role_filter_list()

    def get_user_location_filter_list(self, query):
        object = self.attributes['object_factory'].create_user_object(
            'GetUserByLocationFilter',
            object_factory=self.attributes['object_factory'],
            user_model=self.attributes['user_model'],
            query=query,
            location_params=self.attributes['location_params']
        )
        return object.get_user_by_location_filter()

    def get_user_role_filter_list(self, query):
        object = self.attributes['object_factory'].create_user_object(
            'GetUserByRoleFilter',
            object_factory=self.attributes['object_factory'],
            user_model=self.attributes['user_model'],
            query=query,
            role_params=self.attributes['role_params']
        )
        return object.get_user_by_role_filter()

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

        # return json.dumps(self.gql_json_parser(result))

        return self.json_parser_get_list(result)


