from flask import Blueprint, request, render_template
import random
import os
import pandas as pd

datas = pd.read_excel(os.path.join(os.getcwd(), '..', 'kelompok-b', 'hasil-kelompok-B.xlsx'))
router = Blueprint('route', __name__, template_folder='template')

@router.route('/')
def index():
  return render_template('index.html')

@router.route('/search')
def search():
  keyword = request.args.get('q')
  sentiments = [0, 0, 0]
  for idx in datas[datas['2: Tweet'].str.contains(keyword)].index:
    sentiment = datas['Sentiment'][idx]
    if sentiment == 'negatif':
      sentiments[0] += 1
    elif sentiment == 'netral':
      sentiments[1] += 1
    else:
      sentiments[2] += 1
  return render_template('search.html', keyword=keyword, data=sentiments)
