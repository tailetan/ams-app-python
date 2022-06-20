class NameSort:
    def __init__(self, **kwargs):
        self.attributes = kwargs

    def sort(self):
        if self.attributes['sort_direction'] == 'asc':
            return self.attributes['query'].order(self.attributes['model'].full_name, self.attributes['model'].key)
        elif self.attributes['sort_direction'] == 'desc':
            return self.attributes['query'].order(-self.attributes['model'].full_name, self.attributes['model'].key)
        else:
            return None
