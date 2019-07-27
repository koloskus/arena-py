import pytest
import requests #pylint: disable=import-error
import sample_credentials

@pytest.mark.parametrize("test_input, url_end, expected", [
    (sample_credentials.block_id, '', 200),
    (sample_credentials.block_id, '/channels', 200),
    ])
def test_get_channel(test_input, url_end, expected):
    response = requests.get('http://api.are.na/v2/blocks/' + str(test_input) + url_end)
    assert response.status_code == expected