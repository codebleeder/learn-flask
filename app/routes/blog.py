__author__ = 'sharads'

from flask import Blueprint, render_template

blog = Blueprint('blog', __name__, url_prefix='/blog')


@blog.route('/')
def blog_page():
    """the blog page"""
    return render_template('blog.html')
