class Image():
    def __init__(self, i):
        self.filename = i['filename']
        self.content_type = i['content_type']
        self.updated_at = i['updated_at']
        self.thumb = i['thumb']
        self.square = i['square']
        self.display = i['display']
        self.large = i['large']
        self.original = i['original']