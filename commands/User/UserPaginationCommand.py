from commands.PaginationCommand import PaginationCommand


class UserPaginationCommand(PaginationCommand):
    def __init__(self, **kwargs):
        self._attributes = kwargs

    def next_page_url(self):
        self._attributes['UserNextPageUrl'].next_page_url(
            query=self._attributes['query'],
            cursor=self._attributes['cursor'],
            location_params=self._attributes['location_params'],
            role_params=self._attributes['role_params'],
            sort_params=self._attributes['sort_params'],
            sort_direction=self._attributes['sort_direction']
        )
