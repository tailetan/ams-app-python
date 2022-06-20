from IFilter import *


class LocationFilter(IFilter):
    def __init__(self, **kwargs):
        self.attributes = kwargs

    def filter(self):
        return (self.attributes['query']
                .filter(self.attributes['model'].location.IN(self.attributes['param_values'])))
