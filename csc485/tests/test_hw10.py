import pytest
from csc485.projects.hw10.fruit_query import is_it_a_fruit


def test_expected():
    assert is_it_a_fruit('apple')


def test_wrongdata_handling():
    assert is_it_a_fruit(9)


def test_case_handling():
    assert is_it_a_fruit('pEar')


def test_mispell_handling():
    assert is_it_a_fruit('banana')
