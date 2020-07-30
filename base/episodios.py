from bs4 import BeautifulSoup
from flask_restful import Resource
from models.episodio import EpisodioModel

class Episodios(Resource):
    def _parse(self, html, container="ultEpsContainer") -> list:
        try:
            episodios = list()
            bs = BeautifulSoup(html, 'html.parser')
            eps = bs.find_all(class_=container)
            if len(eps) == 0:
                eps = bs.find(id="aba_epi")
            else:
                eps = eps[1]
            for ep in eps.find_all(class_="ultEpsContainerItem"):
                link = ep.a
                episodio = EpisodioModel(
                    image=link.img.get('data-lazy-src'),
                    name=link.get('title'),
                    link=link.get('href')
                )
                episodios.append(episodio.to_dict())
            return episodios
        except Exception as e:
            raise e
