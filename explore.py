import requests
import user
import channel
import block

class All:
    def __init__(self, a):
        self.term = a.get('term')
        self.per = a.get('per')
        self.current_page = a.get('current_page')
        self.total_pages = a.get('total_pages')
        self.length = a.get('length')
        self.authenticated = a.get('authenticated')
        self.channels = []
        for ch in a.get('channels'):
            # if (ch.get('kind') == 'default'):
            self.channels.append(ch.get('slug'))
        print(self.channels)
        self.blocks = a.get('blocks')
        self.users = a.get('users')

def getAll(terms):
    print('Getting http://api.are.na/v2/channels/' + terms)
    r = requests.get('http://api.are.na/v2/channels/' + terms)
    print(r)
    return All(r.json())