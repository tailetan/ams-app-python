class GetUserFilterDecorator:
    def __init__(self, **kwargs):
        self.attributes = kwargs

    def query_location_filter(self, query):
        result = self.attributes['object_factory'].create_filter_object(
            'FilterLocationRequest',
            object_factory=self.attributes['object_factory'],
            query=query,
            location_params=self.attributes['location_params']).filter_location_request()
        return result

    def query_role_filter(self, query):
        result = self.attributes['object_factory'].create_filter_object(
            'FilterRoleRequest',
            object_factory=self.attributes['object_factory'],
            query=query,
            role_params=self.attributes['role_params']).filter_role_request()
        return result

    def get_user_location_role_filter_list(self):
        query_location_filter = self.query_location_filter(
            self.attributes['query'])
        query_role_filter = self.query_role_filter(query_location_filter)
        return query_role_filter
