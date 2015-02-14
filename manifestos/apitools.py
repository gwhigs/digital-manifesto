import csv
import requests
import time
import math

from django.conf import settings

__author__ = 'gwhigs'


OMEKA_ENDPOINT = settings.OMEKA_ENDPOINT
OMEKA_KEY = settings.OMEKA_API_KEY


def omeka_api_request(resource='items', api_key=OMEKA_KEY, endpoint=OMEKA_ENDPOINT, **kwargs):
    url = '/'.join((endpoint, resource, ''))
    params = {'key': api_key}
    params.update(kwargs)
    resp = requests.get(url, params=params)
    return resp


def get_all_pages(pages):
    _data = []
    page = 1
    while page <= pages:
        print('Getting results page ' + str(page) + ' of ' + str(pages) + ' ...')
        params = {'page': str(page), 'per_page': '50'}
        resp = omeka_api_request(**params)
        _data.extend(resp.json())
        page += 1
        time.sleep(2)
    return _data


def get_all(resource='items'):
    response = omeka_api_request(resource=resource)
    results = int(response.headers['omeka-total-results'])
    print('{} results found.'.format(results))
    pages = math.ceil(results/50)
    _data = get_all_pages(pages)
    return _data


def handle_omeka(omeka_data):
    """
    General handling normally done every time after we grab Omeka data
    via the API with get_all.
    """
    for obj in omeka_data:
        # Handle the weird 'element_texts' format by flattening as best we can
        if 'element_texts' in obj:
            for element_text in obj['element_texts']:
                key = element_text['element']['name']
                value = element_text['text']
                obj[key] = value
        # Flatten out other misc dicts
        for obj_key, obj_val in obj.copy().items():
            if obj[obj_key] and type(obj_val) is dict:
                for key, value in obj_val.items():
                    obj[obj_key + '_' + key] = obj[obj_key][key]
            if type(obj_val) is dict or not obj_val:
                del obj[obj_key]
    return omeka_data


def make_csv(json_resp, resource='items'):
    for obj in json_resp:
        if 'tags' in obj and obj['tags']:
            tags = [tag['name'] for tag in obj['tags']]
            obj['tags'] = ', '.join(tags)
    _data = handle_omeka(json_resp)

    fn = resource + '_output.csv'
    with open(fn, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, sorted(_data.keys()), extrasaction='ignore')
        writer.writeheader()
        for obj in json_resp:
            writer.writerow({k: v for k, v in obj.items()})
        print('File created: {}'.format(fn))

if __name__ == '__main__':
    from pprint import pprint
    resource_name = 'items'
    data = get_all(resource=resource_name)
    d = data[11]
    print(d)
    pprint(d)
    make_csv(data, resource=resource_name)