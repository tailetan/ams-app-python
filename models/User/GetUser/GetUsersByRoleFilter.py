class GetUserByRoleFilter():
    def __init__(self, **kwargs):
        self.attributes = kwargs

    def get_user_by_role_filter(self):
        obj = self.attributes['object_factory'].create_filter_object(
            'FilterRoleRequest',
            model=self.attributes['model'],
            object_factory=self.attributes['object_factory'],
            query=self.attributes['query'],
            role_params=self.attributes['role_params']
        )
        return obj.filter_role_request()
