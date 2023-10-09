from csc485.projects.hw11.get_casual_fruit import get_formal_name
import pytest


@pytest.mark.parametrize('test_data,expected',
                         [('apple', 'Malus domestica'), (3, 'fruit not on list'), ('cantaloupe', 'fruit not on list'),
                          ('Apple', 'Malus domestica'), ('', 'fruit not on list')])
def test_parametrized(test_data,expected):
    assert get_formal_name(test_data) == expected
