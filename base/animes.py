from bs4 import BeautifulSoup
from flask_restful import Resource
from models.anime import AnimeModel

class Animes(Resource):
    def _parse(self, html, container="ultAnisContainer") -> list:
        try:
            animes = list()
            bs = BeautifulSoup(html, 'html.parser')
            anime = bs.find(class_=container)
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
