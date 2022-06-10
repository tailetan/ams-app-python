from decorators.FilterDecorator import *


class RoleFilterDecorator(FilterDecorator):
    def __init__(self, **kwargs):
        self.attributes = kwargs

    def filter(self):
        return (self.attributes['query']
                .filter(self.attributes['model'].role.IN(self.attributes['param_values'])))
