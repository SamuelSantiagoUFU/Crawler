class AnimeModel(object):
    def __init__(self, **fields):
        self.image: str = fields.get('image', None)
        self.name: str = fields.get('name', None)
        self.link: str = fields.get('link', None)
        self.infos: dict = fields.get('infos', {'views':0,'time':'0:00','rating':'0%'})

    def to_dict(self) -> dict:
        return self.__dict__
