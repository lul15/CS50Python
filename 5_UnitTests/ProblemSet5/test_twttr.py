from twttr import shorten


def test_word():
    assert(shorten("Twitter")) == "Twttr"


def test_phrase():
    assert(shorten("What's your name?")) == "Wht's yr nm?"


def test_mixed_input():
    assert(shorten("CS50")) == "CS50"


def test_sentence():
    assert(shorten("Just setting Up my twttr")) == "Jst sttng p my twttr"

