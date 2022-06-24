class Total():
    def total(self, **kwargs):
        return int(kwargs['query'].count())
