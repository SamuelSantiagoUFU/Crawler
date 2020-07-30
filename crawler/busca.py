import requests
from base.animes import Animes

class Crawler(Animes):
    def __init__(self, busca):
        self.busca = busca
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
        base_url = 'https://meusanimes.com/'
        payload = {'s': self.busca}
        r = requests.get(base_url, params=payload)
        self.response['data'] = self._parse(r.text, "loopAnimes")
