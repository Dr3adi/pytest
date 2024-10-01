import pytest
import requests


@pytest.fixture
def len_list(request):
    s = [1, 2, 3, 4, 5, 6, 7, 8]

    def finalizer():
        print("\nfinalizer")

    request.addfinalizer(finalizer)
    return s


@pytest.fixture
def get_url_dog_api():
    r = requests.get('https://dog.ceo/api/breeds/image/random')
    return r
