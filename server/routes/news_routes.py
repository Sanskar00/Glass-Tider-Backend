from flask import Blueprint
from utils.news_utils import theHindu,econmicTimes,bussinessToday
import random

news_routes=Blueprint('news_routes',__name__)
@news_routes.route('/news')
def news():
    articles=theHindu()+econmicTimes()+bussinessToday()
    random.shuffle(articles)
    return {"array":articles}