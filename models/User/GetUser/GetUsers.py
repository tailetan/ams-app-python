import json
from models.BaseModel import *


class GetUsers(BaseModel):
    def __init__(self, **kwargs):
        self.attributes = kwargs

    def get_all_user(self):
        query = self.attributes['user_model'].query()
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

    def create_sort_query(self, **kwargs):
        sort_object = self.attributes['object_factory'].create_sort_object(
            'Sort',
            model=self.attributes['user_model'],
            sort_params=self.attributes['sort_params'],
            query=kwargs['query'],
            sort_direction=kwargs['sort_direction']
        )

        return sort_object.sort()

    def create_user_params_url(self):
        url = self.attributes['object_factory'].create_user_object(
            'UserParamsUrl',
            location_params=self.attributes['location_params'],
            role_params=self.attributes['role_params'],
        )

        return url.create_params_url()

    def get_users(self):
        if (self.attributes['location_params'][0] == 'None'
                and self.attributes['role_params'][0] == 'None'):
            filter_query = self.get_all_user()
        elif self.attributes['location_params'][0] == 'None':
            filter_query = self.get_user_role_filter_list(
                self.get_all_user())
        elif self.attributes['role_params'][0] == 'None':
            filter_query = self.get_user_location_filter_list(
                self.get_all_user())
        else:
            filter_query = self.get_user_location_role_filter_list(
                self.get_all_user())

        self.attributes['object_factory'].create_pagination_object(
            'PaginationTemplate',
            object_factory=self.attributes['object_factory'],
            query=filter_query,
            model=self.attributes['user_model'],
            page=self.attributes['page'],
            invoker=self.attributes['invoker'],
            location_params=self.attributes['location_params'],
            role_params=self.attributes['role_params'],
            sort_params=self.attributes['sort_params'],
            sort_direction=self.attributes['sort_direction'],
            search_key=self.attributes['search_key'],
            search_value=self.attributes['search_value'],
            model_name_url=self.attributes['model_name_url']
        )
        # Sort
        sort_query = self.create_sort_query(
            query=filter_query,
            sort_direction=self.attributes['sort_direction']
        )
        if self.attributes['sort_direction'] == 'asc':
            r_sort_query = self.create_sort_query(
                query=filter_query,
                sort_direction='desc'
            )
        else:
            r_sort_query = self.create_sort_query(
                query=filter_query,
                sort_direction='asc'
            )

        # Pagination
        pagination_object = self.attributes['object_factory'].create_user_object(
            'UserPagination',
            model=self.attributes['user_model'],
            query=sort_query,
            r_query=r_sort_query,
            page=self.attributes['page'],
            object_factory=self.attributes['object_factory'],
            invoker=self.attributes['invoker'],
            cursor=self.attributes['cursor'],
            location_params=self.attributes['location_params'],
            role_params=self.attributes['role_params'],
            sort_params=self.attributes['sort_params'],
            sort_direction=self.attributes['sort_direction'],
            search_key=self.attributes['search_key'],
            search_value=self.attributes['search_value'],
            model_name_url=self.attributes['model_name_url']
        )
        (
            total, per_page, current_page, last_page, from_result, to_result,
            first_page_url, last_page_url, prev_page_url, next_page_url,
            items
        ) = pagination_object.paginate()

        # Result
        return self.json_parser_get_list(
            total=total,
            per_page=per_page,
            current_page=current_page,
            last_page=last_page,
            from_result=from_result,
            to_result=to_result,
            first_page_url=first_page_url,
            last_page_url=last_page_url,
            next_page_url=next_page_url if to_result != total else "",
            prev_page_url=prev_page_url if from_result > 1 else "",
            query_obj=items
        )
        # print(to_result,total)

