import re
import requests
from bs4 import BeautifulSoup
from flask_restful import Resource
from models.anime import AnimeModel

class Crawler(Resource):
    def __init__(self, page=1):
        self.page = page
        self.response = dict(data=list(), message=None)

    def run(self):
        try:
            self._crawl()
        except Exception as e:
            raise e
        finally:
            pass
        return self.response

    def _crawl(self):
        base_url = 'https://meusanimes.com/lista-de-animes-online/page/{}/'.format(self.page)
        r = requests.get(base_url)
        self.response['data'] = self._parse(r.text)

    def _parse(self, html) -> list:
        try:
            animes = list()
            bs = BeautifulSoup(html, 'html.parser')
            anime = bs.find(class_="ultAnisContainer")
            for an in anime.find_all(class_="ultAnisContainerItem"):
                link = an.a
                ani = AnimeModel(
                    image=link.img.get('data-lazy-src'),
                    name=link.get('title'),
                    link=link.get('href'),
                    eps=link.find(class_="aniEps").get_text()
                )
                animes.append(ani.to_dict())
            return animes
        except Exception as e:
            raise e
