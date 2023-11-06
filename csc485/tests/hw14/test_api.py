"""
testable things:
    part 1:
        is flask app imported properly
    part 2:
        Does api function when given special http characters? ie /
        Does the function fail when given multiple arguments
        Does the function work with a very long string
"""

import json
import pytest
import requests
from csc485.projects.hw14.api import app  # this is the flask app


# this is a pytest fixture
@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


# this is a simplified happy path test
def test_expect_good(client):
    # call the API, get the server response
    response = client.get('/get_strength?password=%%%%%%%')
    assert response.status_code == 200

    # convert the json payload to a dict
    data = json.loads(response.data.decode())

    assert data.get('password') == '%%%%%%%'
    assert data.get('strength') == 'good'


# this is an example very negative test
def test_api_error(client):
    # disambiguate
    password = '#password'

    with pytest.raises(ZeroDivisionError):
        response = client.get(f"/get_strength?password={password}")


def test_app():
    assert app.app_context is not None


@pytest.mark.parametrize(
    'test_data,expected', [
        ('http://127.0.0.1:5000/get_strength?password=/%%/%%%%', 200),
        ('http://127.0.0.1:5000/get_strength?password=pass1?password=pass2', 200),
        ('http://127.0.0.1:5000/get_strength?password=asfasdfasdffasdfas'
         'dfassdfassdfasdfasdfasdfasdfasdf'
         'asdfasdfasdfasdfasdfasdfasdfasdfasdfasdfassfasdfasf'
         'asdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdf'
         'asdfasdfasfasdfasdfasdfasdfasdfassdfasdfasdfasdfasdf', 200)
    ]
)
def test_running(test_data, expected):
    r = requests.get(test_data)
    assert r.status_code == expected
