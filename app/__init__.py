__author__ = 'sharads'

from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True

# import and register Blueprint
from app.routes.home import home
from app.routes.blog import blog
app.register_blueprint(home)
app.register_blueprint(blog)

