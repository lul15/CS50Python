from hello import hello


def test_default():
    assert hello() == "hello, world"

# keep tests simple, so we don't need tests for our test
def test_argument():
    for name in ["Hermione", "Harry", "Ron"]:
        assert hello(name) == f"hello, {name}"
    assert hello("David") == "hello, David"
