import pytest


@pytest.fixture
def len_list(request):
    s = [1, 2, 3, 4, 5, 6, 7, 8]

    def finalizer():
        print("\nfinalizer")
    request.addfinalizer(finalizer)
    return s