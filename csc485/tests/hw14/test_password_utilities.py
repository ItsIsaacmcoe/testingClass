"""
testable items:
    compute_complexity:
        1. does the function work as intended with expected input type?
            1. input test, output 0
            2. input t~$t, output 0
         2. does the function fail when given the wrong data type?
            1. Int
            2. Float
            3. Bool

    evaluate_strength
        1. does the function work as intended with expected input type
            1. input test, output False
            2. input t~$@t, output True
        2. does the function fail when given the wrong data type?
            1. Int
            2. Float
            3. Bool

        3. will evaluate_strength fail if compute_complexity fails?
        4. will the program say a password is strong even if all the
        characters are the same? i.e. all complexifiers


"""

import pytest
from csc485.projects.hw14.password_utilities import (compute_complexity,
                                                     evaluate_strength)


@pytest.mark.parametrize(
    'test_data,expected', [
        ('test', 0), ('t~$t', 50), (1, 0), (2.2, 0), (True, 0)
    ]
)
def test_complexity(test_data, expected):
    assert compute_complexity(test_data) == expected


@pytest.mark.parametrize(
    'test_data,expected', [
        ('test', False), ('t~$@t', True), (1, False),
        (2.2, False), (True, False), ('@@@@', False)
    ]
)
def test_strength(test_data, expected):
    assert evaluate_strength(test_data) == expected
