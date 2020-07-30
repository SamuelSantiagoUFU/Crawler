import requests
import re
from base.episodios import Episodios

class Crawler(Episodios):
    def __init__(self, anime, page=1, pages_per_view=1):
        self.anime = anime
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
        base_url = 'https://meusanimes.com/assistir-gratis/'+self.anime+'/page/{}'
        for page in range(self.page, self.page + self.pages_per_view):
            r = requests.get(base_url.format(page))
            if (r.url != base_url.format(page)):
                base_url = re.search(r"https://meusanimes.com/[\w+-]+/[\w+-]+", r.url).string + "/page/{}"
                r = requests.get(base_url.format(page))
            self.response['data'] += self._parse(r.text)
        self.response['message'] = '{} episódios carregados!'.format(len(self.response['data']))
