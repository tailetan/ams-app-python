class FromTo:
    def __init__(self):
        pass

    def from_result(self, **kwargs):
        from_result = 1
        for i in range(1, int(kwargs['page'])):
            from_result += int(kwargs['per_page'])
        return from_result

    def to_result(self, **kwargs):
        to_result = 0
        from_result = self.from_result(
            page=kwargs['page'],
            per_page=kwargs['per_page']
        )
        to_result = int(from_result) + int(kwargs['per_page']) - 1
        if to_result > int(kwargs['total']):
            to_result = int(kwargs['total'])

        return to_result
