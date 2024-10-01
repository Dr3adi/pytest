def test_len_1(len_list):
    assert len(len_list) == 8


def test_dog_status(get_url_dog_api):
    assert get_url_dog_api.status_code == 200
    data = get_url_dog_api.json()
    assert data['status'] == 'success'
