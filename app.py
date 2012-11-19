import os
from flask import Flask, render_template, jsonify
app = Flask(__name__)

@app.route('/')
def landing_page():
  return render_template('index.html')

@app.route('/pages')
def pages():
  pages = {
      'title': 'Humble Beginnings',
      'content': '<p>Since I do Ruby on Rails for a living now I changed my site back to a Python based framework called <a href="http://flask.pocoo.org/">flask</a>. I miss Python.</p><p>Also Im using <a href="http://twitter.github.com/bootstrap/">Twitter Bootstrap</a> just to upset <a href="http://roguespark.com/">Cameron Sampson</a>.</p>'
  }
  return jsonify(pages)


if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5000))
  app.debug = True
  app.run(host='0.0.0.0', port=port)
