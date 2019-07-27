import pytest
import requests #pylint: disable=import-error
import sample_credentials

class TestUserAPI(object):
    def test_get_user_by_id(self):
        response = requests.get('http://api.are.na/v2/users/' + str(sample_credentials.user_id))
        assert response.status_code == 200
    
    def test_get_all_channels_by_user(self):
        response = requests.get('http://api.are.na/v2/users/' + str(sample_credentials.user_id) + '/channels')
        if response.status_code == 401:
            pytest.xfail('API added requirement for authentication')
        assert response.status_code == 200
    
    def test_get_users_id_channel(self):
        response = requests.get('http://api.are.na/v2/users/' + str(sample_credentials.user_id) + '/channel')
        if response.status_code == 404:
            pytest.xfail('API added requirement for authentication')
        assert response.status_code == 200

    def test_get_users_following(self):
        response = requests.get('http://api.are.na/v2/users/' + str(sample_credentials.user_id) + '/following')
        if response.status_code == 401:
            pytest.xfail('API added requirement for authentication')
        assert response.status_code == 200

    def test_get_users_followers(self):
        response = requests.get('http://api.are.na/v2/users/' + str(sample_credentials.user_id) + '/followers')
        if response.status_code == 401:
            pytest.xfail('API added requirement for authentication')
        assert response.status_code == 200