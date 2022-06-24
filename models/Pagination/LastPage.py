import math


class LastPage:
    def __init__(self):
        pass

    def last_page(self, **kwargs):
        total = float(kwargs['total'])
        per_page = float(kwargs['per_page'])
        last_page = math.ceil((total / per_page))
        return int(last_page)
