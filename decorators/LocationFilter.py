from IFilter import *


class LocationFilter(IFilter):
    def __init__(self, **kwargs):
        self.attributes = kwargs

    def filter(self):
        # result = [x for x in self.attributes['query']
        #           if x['location'] in self.attributes['param_values']]
        # return result

        return (self.attributes['query']
                .filter(self.attributes['model'].location.IN(self.attributes['param_values'])))
