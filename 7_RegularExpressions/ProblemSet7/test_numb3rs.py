from numb3rs import validate


def test_low_valid():
    assert (validate("0.0.0.0")) == True


def test_valid_input():
    assert (validate("127.0.0.1")) == True


def test_valid_input2():
    assert (validate("140.247.235.144")) == True


def test_high_valid():
    assert (validate("255.255.255.255")) == True


def test_invalid_all_octets():
    assert (validate("512.512.512.512")) == False


def test_invalid_first_octet():
    assert (validate("256.255.255.255")) == False


def test_invalid_second_octet():
    assert (validate("0.2000.0.0")) == False


def test_invalid_third_octet():
    assert (validate("0.0.1000.0")) == False


def test_invalid_fourth_octet():
    assert (validate("1.2.3.1000")) == False


def test_multiple_invalid_octets():
    assert (validate("64.128.256.512")) == False


def test_invalid_ipv6():
    assert (validate("2001:0db8:85a3:0000:0000:8a2e:0370:7334")) == False


def test_invalid_str():
    assert (validate("cat")) == False


def test_invalid_input():
    assert (validate("gibberish.continued.gibberish.false")) == False
