# import urllib
#
#
# class UserNextPageUrl():
#     def __init__(self, **kwargs):
#         self._attributes = kwargs
#
#     def next_page_url(self, **kwargs):
#         items, next_curs, more = kwargs['query'].fetch_page(
#             2, start_cursor=kwargs['cursor'])
#         if more:
#             next_c = next_curs.urlsafe()
#         else:
#             next_c = None
#
#         params_url = {
#             "location": ','.join(kwargs['location_params']),
#             "role": ','.join(kwargs['role_params']),
#             "sort_params": kwargs['sort_params'],
#             "sort_direction": kwargs['sort_direction'],
#             "cursor": next_c
#         }
#
#         url = "/user?{}".format(urllib.urlencode(params_url))
#
#         return items, url
