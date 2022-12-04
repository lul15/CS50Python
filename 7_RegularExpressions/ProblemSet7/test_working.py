import pytest


from working import convert


def test_9to5():
    assert (convert("9 AM to 5 PM")) == "09:00 to 17:00"


def test_900am_to_500pm():
    assert (convert("9:00 AM to 5:00 PM")) == "09:00 to 17:00"


def test_10pm_to_8am():
    assert (convert("10 PM to 8 AM")) == "22:00 to 08:00"


def test_1030pm_to_850am():
    assert (convert("10:30 PM to 8:50 AM")) == "22:30 to 08:50"


def test_edge_case():
    assert (convert("12:00 AM to 12:00 PM")) == "00:00 to 12:00"


def test_edge_case2():
    assert (convert("12 AM to 12 PM")) == "00:00 to 12:00"

# TODO - combine tests
def test_value_error():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")


def test_value_error2():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")


def test_value_error3():
    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00 PM")


def test_value_error4():
    with pytest.raises(ValueError):
        convert("10:7 AM - 5:1 PM")


def test_value_error5():
    with pytest.raises(ValueError):
        convert("09:00 to 17:00")


def test_value_error6():
    with pytest.raises(ValueError):
        convert("9AM to 5PM")
