import requests
from base.animes import Animes

class Crawler(Animes):
    def __init__(self, page=1, pages_per_view=1):
        self.page = page
        self.pages_per_view = pages_per_view
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
        base_url = 'https://meusanimes.com/lista-de-animes-online/page/{}/'
        for page in range(self.page, self.page + self.pages_per_view):
            r = requests.get(base_url.format(page))
            self.response['data'] += self._parse(r.text)
        self.response['message'] = '{} animes carregados!'.format(len(self.response['data']))
