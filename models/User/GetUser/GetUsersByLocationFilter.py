class GetUserByLocationFilter():
    def __init__(self, **kwargs):
        self.attributes = kwargs

    def get_user_by_location_filter(self):
        obj = self.attributes['object_factory'].create_filter_object(
            'FilterLocationRequest',
            object_factory=self.attributes['object_factory'],
            model=self.attributes['user_model'],
            query=self.attributes['query'],
            location_params=self.attributes['location_params']
        )
        return obj.filter_location_request()
