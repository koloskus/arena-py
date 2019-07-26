import requests
import user
import image

class Block():
    def __init__(self, b):
        self.id = b.get('id')
        self.title = b.get('title')
        self.updated_at = b.get('updated_at')
        self.created_at = b.get('created_at')
        self.metadata = b.get('metadata')
        self.base_class = b.get('base_class')
        self.block_class = b.get('class')
        # if self.base_class != 'Channel':
        self.state = b.get('state')
        self.comment_count = b.get('comment_count')
        self.generated_title = b.get('generated_title')
        self.content_html = b.get('content_html')
        self.description_html = b.get('description_html')
        self.visibility = b.get('visibility')
        self.content = b.get('content')
        self.description = b.get('description')
        self.source = b.get('source')
        if (self.block_class == 'Image'):
            self.image = image.Image(b.get('image'))
        self.embed = b.get('embed')
        self.attachment = b.get('attachment')
        #named 'block_class' because of built-in conflict with .class
        self.user = user.User(b.get('user'))
        #self.connections = b.get('connections')
        # connections doesn't seem to exist in a block when gathered from Channel['Contents']