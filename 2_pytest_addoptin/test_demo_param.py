# команда запуска параметризованного теста: pytest .\2_pytest_addoptin\ --url=ya.ru -s
# можно использовать для упровления тестовыми стендами
def test_answer(url_param):
    if url_param == "ya.ru":
        print("yandex")
    elif url_param == "google.com":
        print("google")
    else:
        print("fuck")