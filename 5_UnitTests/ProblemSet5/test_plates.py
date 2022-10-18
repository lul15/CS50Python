from plates import is_valid


def test_start_with_two_letters():
    assert (is_valid("CS50")) == True


def test_not_start_with_two_letters():
    assert (is_valid("50CS")) == False


def test_plate_length():
    assert (is_valid("AAA222")) == True


def test_incorrect_plate_length():
    assert (is_valid("50PYTHON")) == False


def test_numbers_in_plate():
    assert (is_valid("AAA22A")) == False


def test_zero_in_mid():
    assert (is_valid("PY05")) == False


def test_numbered_plates():
    assert (is_valid("12345")) == False


def test_special_chars():
    assert (is_valid("PI3.14")) == False
    assert (is_valid("H")) == False
    assert (is_valid("CS50%")) == False
