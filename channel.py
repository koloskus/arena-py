import requests
from user import User

class Channel:
    def __init__(self, slug):
        r = requests.get('http://api.are.na/v2/channels/' + slug)
        c = r.json()
        self.title = c['title']
        self.id = c['id']
        self.created = c['created_at']
        self.updated = c['updated_at']
        self.added_to_at = c['added_to_at']
        self.is_published = c['published']
        self.is_open = c['open']
        self.collaboration = c['collaboration']
        self.collaborator_count = c['collaborator_count']
        self.slug = c['slug']
        self.length = c['length']
        self.kind = c['kind']
        self.status = c['status']
        self.user_id = c['user_id']
        self.manifest = c['manifest']
        self.contents = c['contents']
        self.base_class = c['base_class']
        #self.page = c['page']
        #self.per = c['per']
        self.collaborators = c['collaborators']
        self.followers = c['follower_count']
        self.share_link = c['share_link']
        self.metadata = c['metadata']
        self.class_name = c['class_name']
        self.can_index = c['can_index']
        self.nsfw = c['nsfw?']
        self.user = User(c['user'])
        print(self.user.id)