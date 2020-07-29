from flask import Flask, jsonify
from flask_restful import Api
from crawler.lancamentos import Crawler as CrawlerL
from crawler.animes import Crawler as CrawlerA

app = Flask(__name__)
api = Api(app)

@app.route('/episodios/lancamento')
def lancamentoEpi():
    crawler = CrawlerL()
    return jsonify(crawler.run())
@app.route('/animes/<int:page>')
def animes(page):
    crawler = CrawlerA(page)
    return jsonify(crawler.run())

if (__name__ == '__main__'):
    app.run(debug=True)
