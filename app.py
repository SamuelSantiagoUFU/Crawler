from flask import Flask, jsonify
from flask_restful import Api
from crawler.lancamentos import Crawler as CrawlerL
from crawler.filmes import Crawler as CrawlerF
from crawler.busca import Crawler as CrawlerB
from crawler.animeq import Crawler as CrawlerAQ

app = Flask(__name__)
api = Api(app)
@app.route('/episodios/<busca>')
def buscar(busca):
    crawler = CrawlerB(busca)
    return jsonify(crawler.run())
@app.route('/filmes', methods=['GET'])
def filmes():
    crawler = CrawlerF('filmes')
    return jsonify(crawler.run())
@app.route('/legendados/lancamentos', methods=['GET'])
def lancamentosL():
    crawler = CrawlerL('legendados')
    return jsonify(crawler.run())
@app.route('/legendados/<palavra>', methods=['GET'])
def buscaLegendados(palavra):
    crawler = CrawlerAQ('legendados', palavra)
    return jsonify(crawler.run())
@app.route('/dublados/lancamentos', methods=['GET'])
def lancamentosD():
    crawler = CrawlerL('dublados')
    return jsonify(crawler.run())

if (__name__ == '__main__'):
    app.run(debug=True)
