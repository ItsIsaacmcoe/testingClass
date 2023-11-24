"""
Items for testing:
    get:
        happy path
            status code
            strength test
        sad path
            leading #
    post:
        happy path
        too many arguments
"""
from csc485.projects.hw15.api import app
import pytest


@pytest.fixture
def client_get_endpoint():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_happy_get(client_get_endpoint):
    response = client_get_endpoint.get('/get_strength?password=hell00000')
    assert response.status_code == 200


def test_happy_get_strength(client_get_endpoint):
    response = client_get_endpoint.get('/get_strength?password=h__ll@@')
    assert response.json == {'password': 'h__ll@@', 'strength': 'good'}


def test_get_type_err(client_get_endpoint):
    with pytest.raises(ZeroDivisionError):
        response = client_get_endpoint.get('/get_strength?password=#helloo')
        assert response.status_code == 200


@pytest.fixture
def client_post_endpoint():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


@pytest.mark.parametrize(
    'test_data,expected', [
        ({'password': 'example'}, 200),
        ({'password': 'example', 'test': 'test'}, 200)
    ]
)
def test_happy_post(client_post_endpoint, test_data, expected):
    payload = test_data
    res = client_post_endpoint.post('/get_strength', json=payload)
    assert res.status_code == expected
