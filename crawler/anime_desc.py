import sys
import requests
import re
from bs4 import BeautifulSoup
from flask_restful import Resource
from models.anime import AnimeModel
from utils.urls import urls

class Crawler(Resource):
    def __init__(self, anime):
        self.anime = re.sub(r"\s+|\+", "-", anime)
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
        base_url = 'https://meusanimes.com/{}/{}'
        for url in urls:
            r = requests.get(base_url.format(url, self.anime))
            if r.status_code == 200:
                break
        if r.status_code != 200:
            self.response['message'] = 'Não foi encontrado nenhum anime!'
            return
        self.response['data'] = self._parse(r.text)
        self.response['data']['link'] = r.url
        self.response['message'] = 'Anime carregado com sucesso!'

    def _parse(self, html):
        try:
            bs = BeautifulSoup(html, 'html.parser')
            anime = bs.find(class_="pageAnimeSection")
            # Informação da esquerda
            capa = anime.find(class_="animeCapa").img.get('data-lazy-src')
            ani = AnimeModel()
            for info in anime.find_all(class_="animeInfo"):
                if m := re.search(r"Autor: (.*)", info.get_text(), re.I):
                    ani.autor = m.group(1)
                    continue
                if m := re.search(r"Est[uú]dio: (.*)", info.get_text(), re.I):
                    ani.estudio = m.group(1)
                    continue
                if m := re.search(r"Diretor: (.*)", info.get_text(), re.I):
                    ani.diretor = m.group(1)
                    continue
                if m := re.search(r"Ano: (.*)", info.get_text(), re.I):
                    ani.ano = m.group(1)
                    continue
                if m := re.search(r"Epis[oó]dios: (.*)", info.get_text(), re.I):
                    ani.eps = m.group(1)
                    continue
                if m := re.search(r"Ovas\/especiais: (.*)", info.get_text(), re.I):
                    ani.ovas_especiais = m.group(1)
                    continue
                if m := re.search(r"Filmes: (.*)", info.get_text(), re.I):
                    ani.filmes = m.group(1)
                    continue
            # Informação da direita
            nome = anime.find(class_="animeFirstContainer").h1.get_text()
            status = anime.find(class_="animeStatus").b.get_text()
            generos = [gen.a.get_text() for gen in anime.find(class_="animeGen").find_all("li")]
            sinopse = anime.find(class_="animeSecondContainer").p.get_text()
            ani.image = capa
            ani.name = nome
            ani.status = status
            ani.generos = generos
            ani.sinopse = sinopse.strip()
            return ani.to_dict()
        except Exception as e:
            raise e
