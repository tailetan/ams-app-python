class FilterRoleRequest:
    def __init__(self, **kwargs):
        self.attributes = kwargs

    def filter_role_request(self):
        role_filter_object = self.attributes['object_factory'].create_filter_object(
            'RoleFilterDecorator',
            model=self.attributes['model'],
            query=self.attributes['query'],
            param_values=self.attributes['role_params']
        )

        result = self.attributes['object_factory'].create_filter_object(
            'FilteredList').filter_request(role_filter_object)

        return result
