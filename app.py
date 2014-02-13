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
    },{
      'title': 'Kitch',
      'content': '<p>Recently a fellow programmer and I were sharing our love of cooking and discovered that we both had a the age old problem of balancing a recipe ingredient list, pantry inventory, and shopping list. Particularly whenever you are at the grocery store and you seem to have forgotten key details about whether or not you have tomatoes. Thus, <a href="https://github.com/hankyates/kitch">Kitch</a> was born.</p><p>The tech for this project is exciting. We are going for a thick client using Backbone and redis as a cache. I\'ve used redis before on a larger scale application and even at this smaller scale it offers giant performance increases. Should be a fun project. Keep tuned for updates.</p>'
    },{
      'title': 'This site is moving',
      'content': 'Just a heads up that I\'ve moved my blog over to <a href="http://blog.hankyates.com">blog.hankyates.com</a> and this site will shortly be turning into a portfolio site. Check my blog for updates on the progress!'
    }
  return make_response(dumps(pages[::-1]))

if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5000))
  app.debug = True
  app.run(host='0.0.0.0', port=port)
