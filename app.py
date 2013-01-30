import os
from json import dumps
from flask import Flask, render_template, make_response
app = Flask(__name__)

@app.route('/')
def landing_page():
  return render_template('index.html')

@app.route('/pages')
def pages():
  pages = {
      'title': 'Humble Beginnings',
      'content': '<p>Since I do Ruby on Rails for a living now I changed my site back to a Python based framework called <a href="http://flask.pocoo.org/">flask</a>. I miss Python.</p><p>Also I\'m using <a href="http://twitter.github.com/bootstrap/">Twitter Bootstrap</a> just to upset <a href="http://roguespark.com/">Cameron Sampson</a>.</p>'
    },{
      'title': 'What should I use for persistence?',
      'content': '<p>Right now I\'m just hardcoding in a hash to my flask application to generate content. Seems like if I ever get serious about blogging I should break my content posts into some sort of db. Postgres seems like overkill since all I\'ll ever have for content is text and a title and a content. Maybe Redis or MongoDB?</p>'
    },{
      'title': 'DataTrail',
      'content': '<p>An old friend of mine, <a href="http://derekgpoole.wordpress.com/">Derek Poole</a>, and I decided to start being creative again. This time instead of <a href="http://www.myspace.com/notvsintheocean">music</a>, we decided to tell a story with a video game. Thus <a href="https://github.com/hankyates/datarail">DataTrail</a> was born.</p><p>As far as tech is concerned I am using <a href="http://requirejs.org/">Require</a> and <a href="http://backbonejs.org/">Backbone</a>. Originally I was using <a href="http://craftyjs.com/">Crafty</a>, but after a co-worker pointed me towards <a href="http://www.createjs.com/#!/CreateJS">CreateJs</a>, I have been refactoring my code to use it instead. Being a fan of micro frameworks, I like the control of something light and modular like CreateJs. Hopefully our proof of concept demo will be up soon!</p> '
    }
  return make_response(dumps(pages[::-1]))

if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5000))
  app.debug = True
  app.run(host='0.0.0.0', port=port)
