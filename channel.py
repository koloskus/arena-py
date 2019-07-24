import requests

class Channel:
    def __init__(self, slug):
        r = requests.get('http://api.are.na/v2/channels/' + slug)
        c = r.json()
        self.title = c['title']
        self.id = c['id']
        self.created = c['created_at']
        self.updated = c['updated_at']
        self.addedToAt = c['added_to_at']
        self.isPublished = c['published']
        self.isOpen = c['open']
        self.collaboration = c['collaboration']
        self.collaboratorCount = c['collaborator_count']
        self.slug = c['slug']
        self.length = c['length']
        self.kind = c['kind']
        self.status = c['status']
        self.userID = c['user_id']
        self.manifest = c['manifest']
        self.contents = c['contents']
        self.baseClass = c['base_class']
        #self.page = c['page']
        #self.per = c['per']
        self.collaborators = c['collaborators']
        self.followers = c['follower_count']
        self.shareLink = c['share_link']
        self.metadata = c['metadata']
        self.className = c['class_name']
        self.canIndex = c['can_index']
        self.nsfw = c['nsfw?']
        self.user = c['user']