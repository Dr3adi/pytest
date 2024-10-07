import pytest
import requests
import json


def test_len_1(len_list):
    assert len(len_list) == 8


def test_dog_status(get_url_dog_api):
    new_url = get_url_dog_api + '/api/breeds/image/random'
    url_api = requests.get(new_url)
    assert url_api.status_code == 200
    data = url_api.json()
    assert data['status'] == 'success'


@pytest.mark.parametrize("count_images", [2, 3, 4, 5])
def test_dog_with_params(get_url_dog_api, count_images):
    new_url = f'{get_url_dog_api}/api/breeds/image/random/{count_images}'
    url_api = requests.get(new_url)
    data = url_api.json()
    print(f'\n{json.dumps(data, indent=4)}')
    assert len(data['message']) == count_images and data['status'] == 'success'


@pytest.mark.parametrize("breeds_list", ['african', 'boxer', 'husky'])
def test_breeds(get_url_dog_api, breeds_list):
    new_url = f'{get_url_dog_api}/api/breed/{breeds_list}/images/random'
    url_api = requests.get(new_url)
    data = url_api.json()
    assert breeds_list in new_url
    assert data['status'] == 'success'


# https://www.openbrewerydb.org/documentation/
def test_city_filter():
    url = 'https://api.openbrewerydb.org/v1/breweries'
    params = {'by_city': 'san_diego', 'per_page': 3}
    r = requests.get(url, params=params)
    data = r.json()
    assert len(data) == 3
    for i in data:
        assert i['city'] == 'San Diego'
