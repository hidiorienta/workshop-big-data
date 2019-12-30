from flask import Blueprint, request, render_template
import random

router = Blueprint('route', __name__, template_folder='template')

@router.route('/')
def index():
  return render_template('index.html')

@router.route('/search')
def search():
  keyword = request.args.get('q')
  return render_template('search.html', keyword=keyword, data=[random.randrange(0, 100) for i in range(3)])
