"""
Running against live webapi

Testable things:
    Is the page rendered properly?
        Call the url and make sure the result is 200.
            Passed

    Does the form take input successfully?
        'Post' to the web page and measure output.
            Passed

    Is the page calling the api?
        Test that the api call in lookup_password.
            Passed
"""

import requests
import pytest


@pytest.mark.live_api
def test_proper_page():
    r = requests.get('http://127.0.0.1:8080')
    assert r.status_code == 200


@pytest.mark.live_api
def test_input():
    r = requests.post('http://127.0.0.1:8080/lookup_password', data={'password': 'test'})
    assert r.status_code == 200


@pytest.mark.live_api
def test_api_function():
    r = requests.post('http://127.0.0.1:8080/lookup_password', data={'password': 't####st'})
    assert str(r.content).find('good') is not None
