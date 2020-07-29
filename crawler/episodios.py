from bs4 import BeautifulSoup
from flask_restful import Resource
from models.episodio import EpisodioModel

class Episodio(Resource):
    def _parse(self, html) -> list:
        try:
            episodios = list()
            bs = BeautifulSoup(html, 'html.parser')
            eps = bs.find_all(class_="listing-videos listing-tube")[0].find_all("li")
            for ep in eps:
                infos = ep.find(class_='listing-infos')
                views = infos.find(class_='views-infos')
                time = infos.find(class_='time-infos')
                rating = infos.find(class_='rating-infos')
                if (not ep.img): continue
                episodio = EpisodioModel(
                    image=ep.img.get('src'),
                    link=ep.a.get('href'),
                    name=ep.a.get('title'),
                    infos={
                        'views':int(views.text) if views is not None else 0,
                        'time':time.text if time is not None else "",
                        'rating':rating.text if rating is not None else ""
                    }
                )
                episodios.append(episodio.to_dict())
            return episodios
        except Exception as e:
            raise e
