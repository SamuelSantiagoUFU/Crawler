import re

class AnimeModel(object):
    def __init__(self, **fields):
        self.image: str = fields.get('image', None)
        self.name: str = fields.get('name', None)
        self.link: str = fields.get('link', None)
        self.eps: str = re.sub("\n", "", fields.get('eps', "0"))

    def to_dict(self) -> dict:
        return self.__dict__
