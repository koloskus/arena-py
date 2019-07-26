import requests

class User:
    def __init__(self, j):
        #r = requests.get('http://api.are.na/v2/users/' + slug)
        c = j#r.json()
        self.id = c['id']
        self.created_at = c['created_at']
        self.slug = c['slug']
        self.username = c['username']
        self.first_name = c['first_name']
        self.last_name = c['last_name']
        self.avatar = c['avatar']
        self.avatar_image = c['avatar_image']
        self.channel_count = c['channel_count']
        self.following_count = c['following_count']
        self.profile_id = c['profile_id']
        self.follower_count = c['follower_count']
        self.initials = c['initials']
        self.can_index = c['can_index']
        self.metadata = c['metadata']
        self.is_premium = c['is_premium']
        self.is_exceeding_private_connections_limit = c['is_exceeding_private_connections_limit']
        self.is_confirmed = c['is_confirmed']
        self.is_pending_reconfirmation = c['is_pending_reconfirmation']
        self.is_pending_confirmation = c['is_pending_confirmation']
        self.badge = c['badge']
        self.base_class = c['base_class']
        self.user_class = c['class']