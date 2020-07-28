import requests
from bs4 import BeautifulSoup
from flask_restful import Resource
from models.anime import AnimeModel

class Crawler(Resource):
    def __init__(self):
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
        base_url = 'https://animeq.online/animes-legendados/'
        payload = {'filtre': 'date'}
        r = requests.get(base_url, params=payload)
        self.response['data'] = self._parse(r.text)

    def _parse(self, html) -> list:
        try:
            animes = list()
            bs = BeautifulSoup(html, 'html.parser')
            eps = bs.find_all(class_="listing-videos listing-tube")[0].find_all("li")
            for ep in eps:
                infos = ep.find(class_='listing-infos')
                views = infos.find(class_='views-infos')
                time = infos.find(class_='time-infos')
                rating = infos.find(class_='rating-infos')
                anime = AnimeModel(
                    image=ep.img.get('src'),
                    link=ep.a.get('href'),
                    name=ep.a.get('title'),
                    infos={
                        'views':int(views.text) if views is not None else 0,
                        'time':time.text if time is not None else "",
                        'rating':rating.text if rating is not None else ""
                    }
                )
                animes.append(anime.to_dict())
            return animes
        except Exception as e:
            raise e
