# Does the program accurately calculate the percentage of special characters
#
# Does the program work when passed an integer?
#
# Does the program work when passed only complexifiers?
#
# Does the program work when an integer is mixed into the string?
import pytest

from csc485.projects.hw11.get_formal_fruit import get_formal_name


# expected
def test_happypath():
    assert get_formal_name('apple')


# int instead of string
def test_wrongtype():
    with pytest.raises(KeyError):
        assert get_formal_name(3)


# misspell or fruit not in list
def test_notinlist():
    with pytest.raises(KeyError):
        get_formal_name('cantaloupe')


# case sensitivity
def test_case():
    with pytest.raises(KeyError):
        get_formal_name('Apple')


# no arguments
def test_empty():
    with pytest.raises(TypeError):
        get_formal_name()
