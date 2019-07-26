import user
import channel
import block

class All:
    def __init__(self, a):
        self.term = a['term']
        self.per = a['per']
        self.current_page = a['current_page']
        self.total_pages = a['total_pages']
        self.length = a['length']
        self.authenticated = a['authenticated']
        self.channels = a['channels']
        self.blocks = a['blocks']
        self.users = a['users']