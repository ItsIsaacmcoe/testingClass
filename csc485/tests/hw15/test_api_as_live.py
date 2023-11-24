"""
Items for testing:
    get:
        happy path
        blank data
        all special characters
    post:
        happy path
        payload with 3 arguments
"""
import requests
import pytest


@pytest.mark.live_api
@pytest.mark.parametrize(
    'test_data,expected', [
        ('http://127.0.0.1:5000/get_strength?password=helloo', 200),
        ('http://127.0.0.1:5000/get_strength?password=', 500),
        ('http://127.0.0.1:5000/get_strength?password=~~~~~~~~~', 200)
    ]
)
def test_live_get(test_data, expected):
    r = requests.get(test_data)
    assert r.status_code == expected


@pytest.mark.live_api
@pytest.mark.parametrize(
    'test_data,expected', [
        ({'password': 'example'}, 200),
        ({'password': 'passowrd', 'test': 'test'}, 200)
    ]
)
def test_live_post(test_data, expected):
    payload = test_data
    res = requests.post('http://127.0.0.1:5000/get_strength', json=payload)
    assert res.status_code == expected
