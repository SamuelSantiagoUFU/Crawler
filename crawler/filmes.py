import requests
from crawler.episodios import Episodio

class Crawler(Episodio):
    def __init__(self, url):
        self.url = url
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
        base_url = 'https://animeq.online/filmes'
        payload = {'filtre': 'date'}
        r = requests.get(base_url, params=payload)
        self.response['data'] = self._parse(r.text)
