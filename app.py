import os
from flask import Flask, jsonify, render_template
from flask_restful import Api
from crawler.lancamentos import Crawler as CrawlerL
from crawler.animes import Crawler as CrawlerA
from crawler.episodios import Crawler as CrawlerEP
from crawler.busca import Crawler as CrawlerB

app = Flask(__name__)
api = Api(app)
@app.route('/doc')
def doc():
    return render_template('doc.html')
@app.route('/episodios/lancamento')
def lancamentoEpi():
    crawler = CrawlerL()
    return jsonify(crawler.run()), 200
@app.route('/anime/<string:anime>/<int:page>')
@app.route('/anime/<string:anime>/<int:page>/<int:pages>')
def episodiosAnime(anime, page=1, pages=1):
    crawler = CrawlerEP(anime, page, pages)
    return jsonify(crawler.run()), 200
@app.route('/animes/<int:page>')
@app.route('/animes/<int:page>/<int:pages>')
def animes(page, pages = 1):
    crawler = CrawlerA(page, pages)
    return jsonify(crawler.run()), 200
@app.route('/animes/<string:busca>')
@app.route('/animes/<string:busca>/<int:page>')
@app.route('/animes/<string:busca>/<int:page>/<int:pages>')
def busca(busca, page = 1, pages = 1):
    crawler = CrawlerB(busca, page, pages)
    return jsonify(crawler.run()), 200
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
