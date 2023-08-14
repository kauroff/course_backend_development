from src.utils import get_data, sort_list, get_date, get_requisites, count_payment, get_description


def test_get_data():
    assert get_data("data.json") == [{"id": 441945886, "state": "EXECUTED", "date": "2019-08-26T10:50:58.294041"},
                                     {"id": 596171168, "state": "EXECUTED", "date": "2018-07-11T02:26:18.671407"},
                                     {"id": 716496732, "state": "EXECUTED", "date": "2018-04-04T17:33:34.701093"},
                                     {"id": 863064926, "state": "EXECUTED", "date": "2019-12-08T22:46:21.935582"},
                                     {"id": 594226727, "state": "EXECUTED", "date": "2018-09-12T21:27:25.241689"},
                                     {"id": 594226727, "state": "CANCELED", "date": "2017-09-12T21:27:25.241689"},
                                     {}
                                     ]


def test_get_date():
    assert get_date({"date": "2019-08-25T10:50:58.294041"}) == "25.08.2019"
    assert get_date({"date": "2017-12-08T10:50:58.294041"}) == "08.12.2017"
    assert get_date({"date": "1996-03-17T10:50:58.294041"}) == "17.03.1996"


def test_get_requisites():
    assert get_requisites("Visa Classic 6831982476737658") == ("Visa Classic", "6831 98** **** 7658")
    assert get_requisites("Счет 72082042523231456215") == ("Счет", "**6215")


def test_count_payment():
    assert count_payment({
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        }
    }) == ("31957.58", "руб.")


def test_get_description():
    assert get_description({"description": "Перевод организации"}) == "Перевод организации"


def test_sort_list():
    assert sort_list([
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041"
        },
        {
            "id": 596171168,
            "state": "EXECUTED",
            "date": "2018-07-11T02:26:18.671407"
        }
    ], 2) == [{"id": 441945886, "state": "EXECUTED", "date": "2019-08-26T10:50:58.294041"},
              {"id": 596171168, "state": "EXECUTED", "date": "2018-07-11T02:26:18.671407"}]
