import re
import requests
from bs4 import BeautifulSoup
from flask_restful import Resource
from models.anime import AnimeModel
from utils.alfabeto import Alfabeto

class Crawler(Resource):
    def __init__(self, url, palavra):
        self.url = url
        self.palavra = palavra
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
        base_url = 'https://animeq.online/animes-{}-online/'.format(self.url)
        r = requests.get(base_url)
        self.response['data'] = self._parse(r.text)

    def _parse(self, html) -> list:
        try:
            animes = list()
            # Pega a primeira letra da palavra
            letra = self.palavra[0]
            # Verifica se é um dígito
            if re.search(r"\d", letra) != None:
                letra = 0
            else:
                letra = Alfabeto.posLetra(letra)
            bs = BeautifulSoup(html, 'html.parser')
            eps = bs.find(id="GTTabs_{}_2472".format(letra))
            print(eps.prettify())
            for ep in eps:
                pass
            return animes
        except Exception as e:
            raise e
