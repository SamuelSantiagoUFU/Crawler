from flask import Flask, jsonify
from flask_restful import Api
from crawler.animeq import Crawler as CrawlerAQ

app = Flask(__name__)
api = Api(app)

@app.route('/lancamentos')
def lancamentos():
    crawler = CrawlerAQ()
    return jsonify(crawler.run())

if (__name__ == '__main__'):
    app.run(debug=True)
