from template_methods.PaginationTemplate import PaginationTemplate


class UserPagination(PaginationTemplate):
    def __init__(self, **kwargs):
        self.attributes = kwargs

    def create_params_url(self):
        url = self.attributes['object_factory'].create_user_object(
            'UserParamsUrl',
            location_params=self.attributes['location_params'],
            role_params=self.attributes['role_params'],
        )

        return url.create_params_url()

    def create_cursor(self):
        forward_cursor_object = self.attributes['object_factory'].create_pagination_object(
            'CreateCursor',
        )
        return forward_cursor_object.create_cursor(
            query=self.attributes['query'],
            r_query=self.attributes['r_query'],
            cursor=self.attributes['cursor'],
            page=self.attributes['page'],
        )
