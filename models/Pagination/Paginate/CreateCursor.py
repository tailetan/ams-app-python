from models.Pagination.RecordsPerPage import RECORDS_PER_PAGE


class CreateCursor:
    # def __init__(self):
    #     pass

    def create_cursor(self, **kwargs):
        results = kwargs['query'].fetch(
            RECORDS_PER_PAGE,
            offset=int(kwargs['page']) * RECORDS_PER_PAGE - RECORDS_PER_PAGE)

        items, cursor, more = kwargs['query'].fetch_page(
            RECORDS_PER_PAGE,
            start_cursor=kwargs['cursor'])
        if more and cursor:
            cursor = cursor

        if int(kwargs['page']) != 1:
            r_items, r_cursor, r_more = kwargs['r_query'].fetch_page(
                RECORDS_PER_PAGE,
                start_cursor=kwargs['cursor'])
            if r_more and r_cursor:
                r_cursor = r_cursor
        else:
            r_cursor = kwargs['cursor']

        return r_cursor.urlsafe(), cursor.urlsafe(), results
