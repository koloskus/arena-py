import pytest
import requests #pylint: disable=import-error
import sample_credentials

@pytest.mark.parametrize("test_input, url_end, expected", [
    ('', '', 200), 
    (sample_credentials.channel_slug, '', 200), 
    (sample_credentials.channel_slug, '/thumb', 200), 
    (sample_credentials.channel_id, '/connections', 200),
    (sample_credentials.channel_id, '/channels', 200),
    (sample_credentials.channel_id, '/contents', 200),
    (sample_credentials.channel_id, '/collaborators', 200)
    ])
def test_get_channel(test_input, url_end, expected):
    response = requests.get('http://api.are.na/v2/channels/' + str(test_input) + url_end)
    assert response.status_code == expected