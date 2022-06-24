import urllib


class CreatePrevPageUrl():
    def create_prev_page_url(self, **kwargs):
        params_url = {
            'sort_params': kwargs['model']._properties[kwargs['sort_params']]._name,
            'sort_direction': kwargs['sort_direction'],
            'cursor': kwargs['cursor'],
            'page': int(kwargs['page']) - 1,
        }
        params_url.update(kwargs['params_url_model'])

        url = '/api/' + kwargs['model_name_url'] + \
            '?{}'.format(urllib.urlencode(params_url))
        return url
