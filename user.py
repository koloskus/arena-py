import requests

class User:
    def __init__(self, u):
        self.id = u['id']
        self.created_at = u['created_at']
        self.slug = u['slug']
        self.username = u['username']
        self.first_name = u['first_name']
        self.last_name = u['last_name']
        self.avatar = u['avatar']
        self.avatar_image = u['avatar_image']
        self.channel_count = u['channel_count']
        self.following_count = u['following_count']
        self.profile_id = u['profile_id']
        self.follower_count = u['follower_count']
        self.initials = u['initials']
        self.can_index = u['can_index']
        self.metadata = u['metadata']
        self.is_premium = u['is_premium']
        self.is_exceeding_private_connections_limit = u['is_exceeding_private_connections_limit']
        self.is_confirmed = u['is_confirmed']
        self.is_pending_reconfirmation = u['is_pending_reconfirmation']
        self.is_pending_confirmation = u['is_pending_confirmation']
        self.badge = u['badge']
        self.base_class = u['base_class']
        self.user_class = u['class']

def getUser(slug):
    r = requests.get('http://api.are.na/v2/users/' + slug)
    return User(r.json())