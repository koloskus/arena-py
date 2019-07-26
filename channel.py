import requests
import user
import block

class Channel:
    def __init__(self, c):
        self.id = c['id']
        self.title = c['title']
        self.created_at = c['created_at']
        self.updated_at = c['updated_at']
        self.added_to_at = c['added_to_at']
        self.published = c['published']
        self.open = c['open']
        self.collaboration = c['collaboration']
        self.collaborator_count = c['collaborator_count']
        self.slug = c['slug']
        self.length = c['length']
        self.kind = c['kind']
        self.status = c['status']
        self.user_id = c['user_id']
        # dict
        self.manifest = c['manifest']
        self.contents = c['contents']
        self.base_class = c['base_class']
        self.page = c['page']
        self.per = c['per']
        self.collaborators = c['collaborators']
        self.follower_count = c['follower_count']
        self.share_link = c['share_link']
        # dict
        self.metadata = c['metadata']
        self.class_name = c['class_name']
        self.can_index = c['can_index']
        self.nsfw = c['nsfw?']
        # dict
        self.user = user.User(c['user'])

def getChannel(slug):
    r = requests.get('http://api.are.na/v2/channels/' + slug)
    return Channel(r.json())