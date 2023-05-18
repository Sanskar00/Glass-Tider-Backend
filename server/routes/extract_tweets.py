from flask import Flask, request, jsonify,Blueprint
from utils.extract_tweets import extractTweets
# import snscrape.modules.twitter as sntwitter
import json

extract_tweets=Blueprint('extract_tweets',__name__)
@extract_tweets.route('/extract_tweets',methods=['post'])
def scrape_tweets():
    # # Search for tweets containing the word
    word=request.data.decode('utf-8')
    print(word)
    tweets=extractTweets(word)
    return {"tweets":tweets}

