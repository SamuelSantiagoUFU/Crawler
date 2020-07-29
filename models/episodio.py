class EpisodioModel(object):
    def __init__(self, **fields):
        self.image: str = fields.get('image', None)
        self.name: str = fields.get('name', None)
        self.link: str = fields.get('link', None)

    def to_dict(self) -> dict:
        return self.__dict__
