import pytest

from um import count


def test0():
    assert (count("yummy")) == 0


def test_empty_input():
    assert (count(" ")) == 0


def test1():
    assert (count("um")) == 1


def test1_multiple_input():
    assert (count("um yummy")) == 1


def test1_multiple_input2():
    assert (count("hello, um, world")) == 1


def test1_specialchars():
    assert (count("um...")) == 1


def test2():
    assert (count("um, hello, um, world")) == 2


def test2_uppercase():
    assert (count("Um, thanks, um...")) == 2


def test1_uppercase():
    assert (count("Um, thanks for the album.")) == 1


def test2_multiple_input():
    assert (count("Um? Mum? Is this that album where, um, umm, the clumsy alums play drums?")) == 2
