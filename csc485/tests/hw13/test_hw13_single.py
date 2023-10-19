from csc485.projects.hw13.compute_complexity import (compute_complexity,
                                                     evaluate_strength)


def test_compute_complexity():
    assert compute_complexity(2.2)


def test_evaluate_strength():
    assert evaluate_strength('log~#@')
