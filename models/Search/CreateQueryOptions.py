from google.appengine.api import search
# from models.Pagination.LimitResultsPerPage import RECORDS_PER_PAGE


class CreateQueryOptions():
    def __init__(self, **kwargs):
        self.attributes = kwargs

    def create_query_options(self):
        if self.attributes['sort_direction'] == 'asc':
            sort = search.SortExpression(
                expression=self.attributes['sort_params'],
                direction=search.SortExpression.ASCENDING,
                default_value="")
        else:
            sort = search.SortExpression(
                expression=self.attributes['sort_params'],
                direction=search.SortExpression.DESCENDING,
                default_value="")
        sort_options = search.SortOptions(expressions=[sort])
        query_options = search.QueryOptions(
            offset=int(self.attributes['offset']),
            # limit=RECORDS_PER_PAGE,
            returned_fields=self.attributes['returned_fields'],
            sort_options=sort_options)
        return query_options
