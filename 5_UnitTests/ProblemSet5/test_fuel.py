import pytest
from fuel import convert, gauge


def test_percentage_conversion():
    assert (convert("3/4")) == 75.0


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
:

def test_value_error():
    with pytest.raises(ValueError):
        convert("cat/dog")


def test_empty_gauge():
    assert (convert("1/100")) == 1.0
    assert (gauge(1)) == "E"


def test_full_gauge():
    assert (convert("99/100")) == 99
    assert (gauge(99)) == "F"


def test_regular_gauge():
    assert (convert("1/2")) == 50
    assert (gauge(50)) == "50%"
