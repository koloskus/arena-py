import requests

class User:
    def __init__(self, u):
        self.id = u.get('id')
        self.created_at = u.get('created_at')
        self.slug = u.get('slug')
        self.username = u.get('username')
        self.first_name = u.get('first_name')
        self.last_name = u.get('last_name')
        self.avatar = u.get('avatar')
        self.avatar_image = u.get('avatar_image')
        self.channel_count = u.get('channel_count')
        self.following_count = u.get('following_count')
        self.profile_id = u.get('profile_id')
        self.follower_count = u.get('follower_count')
        self.initials = u.get('initials')
        self.can_index = u.get('can_index')
        self.metadata = u.get('metadata')
        self.is_premium = u.get('is_premium')
        self.is_exceeding_private_connections_limit = u.get('is_exceeding_private_connections_limit')
        self.is_confirmed = u.get('is_confirmed')
        self.is_pending_reconfirmation = u.get('is_pending_reconfirmation')
        self.is_pending_confirmation = u.get('is_pending_confirmation')
        self.badge = u.get('badge')
        self.base_class = u.get('base_class')
        self.user_class = u.get('class')

def getUser(slug):
    r = requests.get('http://api.are.na/v2/users/' + slug)
    return User(r.json())