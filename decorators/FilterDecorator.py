from IFilter import *


class FilterDecorator(IFilter):
    def __init__(self, obj):
        self.object = obj

    def filter(self):
        pass
