from abc import ABCMeta, abstractmethod


class PaginationTemplate():
    __metaclass__ = ABCMeta

    def __init__(self, **kwargs):
        self.attributes = kwargs

    @staticmethod
    @abstractmethod
    def create_cursor(self):
        pass

    @staticmethod
    @abstractmethod
    def create_params_url(self):
        pass

    def total(self):
        total_object = self.attributes['object_factory'].create_pagination_object(
            'Total')

        return total_object.total(
            query=self.attributes['query']
        )

    def per_page(self):
        per_page_object = self.attributes['object_factory'].create_pagination_object(
            'PerPage')

        return per_page_object.per_page()

    def current_page(self):
        current_page_object = self.attributes['object_factory'].create_pagination_object(
            'CurrentPage')

        return current_page_object.current_page(
            current_page=self.attributes['page']
        )

    def last_page(self, **kwargs):
        last_page_object = self.attributes['object_factory'].create_pagination_object(
            'LastPage')

        return last_page_object.last_page(
            total=kwargs['total'],
            per_page=kwargs['per_page']
        )

    def from_result(self, **kwargs):
        from_object = self.attributes['object_factory'].create_pagination_object(
            'FromTo')

        return from_object.from_result(
            page=self.attributes['page'],
            per_page=kwargs['per_page']
        )

    def to_result(self, **kwargs):
        to_object = self.attributes['object_factory'].create_pagination_object(
            'FromTo')

        return to_object.to_result(
            page=self.attributes['page'],
            per_page=kwargs['per_page'],
            total=kwargs['total'],
        )

    def create_first_page_url(self):
        first_page_url_object = self.attributes['object_factory'].create_pagination_object(
            'CreateFirstPageUrl')

        return first_page_url_object.create_first_page_url(
            model=self.attributes['model'],
            params_url_model=self.create_params_url(),
            sort_params=self.attributes['sort_params'],
            sort_direction=self.attributes['sort_direction'],
            # search_key=self.attributes['search_key'],
            # search_value=self.attributes['search_value'],
            model_name_url=self.attributes['model_name_url']
        )

    def create_last_page_url(self, **kwargs):
        last_page_url_object = self.attributes['object_factory'].create_pagination_object(
            'CreateLastPageUrl')

        return last_page_url_object.create_last_page_url(
            model=self.attributes['model'],
            params_url_model=self.create_params_url(),
            last_page=kwargs['last_page'],
            sort_params=self.attributes['sort_params'],
            sort_direction=self.attributes['sort_direction'],
            # search_key=self.attributes['search_key'],
            # search_value=self.attributes['search_value'],
            model_name_url=self.attributes['model_name_url']
        )

    def create_next_page_url(self, **kwargs):
        next_page_url_object = self.attributes['object_factory'].create_pagination_object(
            'CreateNextPageUrl')

        return next_page_url_object.create_next_page_url(
            model=self.attributes['model'],
            cursor=kwargs['forward_cursor'],
            params_url_model=self.create_params_url(),
            page=self.attributes['page'],
            sort_params=self.attributes['sort_params'],
            sort_direction=self.attributes['sort_direction'],
            # search_key=self.attributes['search_key'],
            # search_value=self.attributes['search_value'],
            model_name_url=self.attributes['model_name_url']
        )

    def create_prev_page_url(self, **kwargs):
        prev_page_url_object = self.attributes['object_factory'].create_pagination_object(
            'CreatePrevPageUrl')

        return prev_page_url_object.create_prev_page_url(
            model=self.attributes['model'],
            cursor=kwargs['backward_cursor'],
            params_url_model=self.create_params_url(),
            sort_params=self.attributes['sort_params'],
            page=self.attributes['page'],
            sort_direction=self.attributes['sort_direction'],
            # search_key=self.attributes['search_key'],
            # search_value=self.attributes['search_value'],
            model_name_url=self.attributes['model_name_url']
        )

    def paginate(self):
        total = self.total()
        per_page = self.per_page()
        current_page = self.current_page()
        last_page = self.last_page(total=total, per_page=per_page)
        from_result = self.from_result(per_page=per_page)
        to_result = self.to_result(per_page=per_page, total=total)
        backward_cursor, forward_cursor, items = self.create_cursor()

        first_page_url = self.create_first_page_url()
        last_page_url = self.create_last_page_url(last_page=last_page)
        prev_page_url = self.create_prev_page_url(
            backward_cursor=backward_cursor
        )
        next_page_url = self.create_next_page_url(
            forward_cursor=forward_cursor
        )
        return (
            total, per_page, current_page, last_page, from_result, to_result,
            first_page_url, last_page_url, prev_page_url, next_page_url,
            items
        )
