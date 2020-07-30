from flask import Flask, jsonify
from flask_restful import Api
from crawler.lancamentos import Crawler as CrawlerL
from crawler.animes import Crawler as CrawlerA
from crawler.busca import Crawler as CrawlerB

app = Flask(__name__)
api = Api(app)

@app.route('/episodios/lancamento')
def lancamentoEpi():
    crawler = CrawlerL()
    return jsonify(crawler.run())
@app.route('/animes/<int:page>')
@app.route('/animes/<int:page>/<int:pages>')
def animes(page, pages = 1):
    crawler = CrawlerA(page, pages)
    return jsonify(crawler.run())
@app.route('/animes/<string:busca>')
def busca(busca):
    crawler = CrawlerB(busca)
    return jsonify(crawler.run())
if (__name__ == '__main__'):
    app.run(debug=True)
