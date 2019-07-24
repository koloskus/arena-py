import requests
import pytest

response = requests.get('http://api.are.na/v2/channels')

def test_response_code():
    assert response.status_code == 200