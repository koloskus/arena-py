import requests
import user
import image

class Block():
    def __init__(self, b):
        self.id = b['id']
        self.title = b['title']
        self.updated_at = b['updated_at']
        self.created_at = b['created_at']
        self.metadata = b['metadata']
        self.base_class = b['base_class']
        if self.base_class != 'Channel':
            self.state = b['state']
            self.comment_count = b['comment_count']
            self.generated_title = b['generated_title']
            self.content_html = b['content_html']
            self.description_html = b['description_html']
            self.visibility = b['visibility']
            self.content = b['content']
            self.description = b['description']
            self.source = b['source']
            self.image = image.Image(b['image'])
            self.embed = b['embed']
            self.attachment = b['attachment']
        #named 'block_class' because of built-in conflict with .class
        self.block_class = b['class']
        self.user = user.User(b['user'])
        #self.connections = b['connections']
        # connections doesn't seem to exist in a block when gathered from Channel['Contents']