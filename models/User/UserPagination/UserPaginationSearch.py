# from models.Search.ReturnedFieldsList import USER_RETURNED_FIELDS
# from template_methods.SearchPaginationTemplate import SearchPaginationTemplate
#
#
# class UserPaginationSearch(SearchPaginationTemplate):
#     def __init__(self, **kwargs):
#         self.attributes = kwargs
#
#     def create_params_url(self):
#         url = self.attributes['object_factory'].create_user_object(
#             'UserParamsUrl',
#             location_params=self.attributes['location_params'],
#             role_params=self.attributes['role_params'],
#         )
#
#         return url.create_params_url()
#
#     def create_offset(self):
#         offset_object = self.attributes['object_factory'].create_pagination_object(
#             'CreateOffsetSearch',
#         )
#         return offset_object.create_offset(
#             query=self.attributes['query'],
#             index_name='User',
#             search_fields_object='CreateUserSearchFields',
#             returned_fields=USER_RETURNED_FIELDS,
#             page=self.attributes['page'],
#             object_factory=self.attributes['object_factory'],
#             search_key=self.attributes['search_key'],
#             search_value=self.attributes['search_value'],
#             sort_params=self.attributes['sort_params'],
#             sort_direction=self.attributes['sort_direction']
#         )
