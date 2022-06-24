from google.appengine.api import search


class Search():
    def __init__(self, **kwargs):
        self.attributes = kwargs

    def search(self):
        create_document_search_object = self.attributes['object_factory'].create_search_object(
            'CreateDocumentSearch',
            index_name=self.attributes['index_name'],
            search_fields_object=self.attributes['search_fields_object'],
            query=self.attributes['query'],
            object_factory=self.attributes['object_factory']
        )
        create_document_search_object.create_document()
        index = search.Index(self.attributes['index_name'])
        for key in self.attributes['search_key']:
            query_string = "%s: %s" % (
                key, self.attributes['search_value'])
            create_query_options_object = self.attributes['object_factory'].create_search_object(
                'CreateQueryOptions',
                returned_fields=self.attributes['returned_fields'],
                sort_params=self.attributes['sort_params'],
                sort_direction=self.attributes['sort_direction'],
                offset=self.attributes['offset'],
            )
            query_options = create_query_options_object.create_query_options()
            query = search.Query(query_string=query_string,
                                options=query_options)
            results = index.search(query)
            number_retrieved = len(results.results)
            if number_retrieved != 0:
                return self.attributes['offset'], results
