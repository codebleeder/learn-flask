__author__ = 'sharads'

from flask import Blueprint, render_template


home = Blueprint('name', __name__)


@home.route('/')
def home_page():
    """
    the home page
    """
    return render_template('home.html')

