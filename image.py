class Image():
    def __init__(self, i):
        self.filename = i.get('filename')
        self.content_type = i.get('content_type')
        self.updated_at = i.get('updated_at')
        self.thumb = i.get('thumb')
        self.square = i.get('square')
        self.display = i.get('display')
        self.large = i.get('large')
        self.original = i.get('original')