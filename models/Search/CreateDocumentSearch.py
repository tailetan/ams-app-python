from google.appengine.api import search


class CreateDocumentSearch():
    def __init__(self, **kwargs):
        self.attributes = kwargs

    def create_document(self):
        index = search.Index(name=self.attributes['index_name'])
        for item in self.attributes['query']:
            create_user_search_field_object = self.attributes['object_factory'].create_search_object(
                self.attributes['search_fields_object'],
                item=item
            )
            index.put(create_user_search_field_object.create_search_fields())
