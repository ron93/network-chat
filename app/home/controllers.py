from flask import Blueprint,render_template,abort 
from jinja2 import TemplateNotFound


module = Blueprint('home', __name__, url_prefix='/home'
               ,template_folder='templates')


@module.route('/')
def home():
    try:
        return render_template('home/home.html')
    except TemplateNotFound:
        abort(404)
