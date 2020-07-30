import requests
from base.episodios import Episodios

class Crawler(Episodios):
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
        base_url = 'https://meusanimes.com'
        r = requests.get(base_url)
        self.response['data'] = self._parse(r.text)
        self.response['message'] = '{} episódios carregados!'.format(len(self.response['data']))
