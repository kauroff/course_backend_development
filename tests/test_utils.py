from src.utils import get_data, sort_list, get_date, get_requisites, count_payment, get_description


def test_get_data():
    assert get_data("data.json") == [{"message":  "haha"}]


def test_get_date():
    assert get_data("2019-08-25T10:50:58.294041") == "25.08.2019"
    assert get_data("2017-12-08T10:50:58.294041") == "08.12.2017"
    assert get_data("1996-03-17T10:50:58.294041") == "17.03.1996"


def test_get_requisites():
    assert get_requisites("Visa Classic 6831982476737658") == "Visa Classic 6831 98** **** 7658"


def test_count_payment():
    assert


def test_get_description():
    assert