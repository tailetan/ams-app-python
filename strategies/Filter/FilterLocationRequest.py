class FilterLocationRequest:
    def __init__(self, **kwargs):
        self.attributes = kwargs

    def filter_location_request(self):
        location_filter_object = self.attributes['object_factory'].create_filter_object(
            'LocationFilter',
            model=self.attributes['model'],
            query=self.attributes['query'],
            param_values=self.attributes['location_params']
        )

        result = self.attributes['object_factory'].create_filter_object(
            'FilteredList').filter_request(location_filter_object)

        return result
