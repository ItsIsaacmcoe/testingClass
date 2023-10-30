import pytest
from csc485.projects.hw12.complexity import compute_complexity

'''
tests:
    String with no complexity.
    String with one special character
    Integer
    String with all special characters
    String with one number in it
'''
@pytest.mark.parametrize(
    'test_data,expected', [('test', 0), ('t$st', 25), (1, 0), ('~@#', 100), ('te1st', 0)])
def test_paths(test_data, expected):
    assert compute_complexity(test_data) == expected
