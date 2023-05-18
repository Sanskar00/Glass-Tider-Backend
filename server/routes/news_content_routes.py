from flask import Blueprint
from flask import request
import requests
from bs4 import BeautifulSoup
from utils.news_content_utils import theHindu,bussinessToday,economictimes
import random


news_content_routes=Blueprint('news_content_routes',__name__)
@news_content_routes.route("/news_content",methods=['post'])
def newsContent():
    request_data=(request.data)
    newsurl=request_data.decode('UTF-8')
    contentrequest=requests.get(newsurl)
    htmlContent=contentrequest.content
    contentSoup=BeautifulSoup(htmlContent,"html.parser")
    if "thehindu" in newsurl:
      content=theHindu(contentSoup)
    
    elif "businesstoday" in newsurl:
       content=bussinessToday(contentSoup)
        
    elif "economictimes" in newsurl:
       content=economictimes(contentSoup)

    return {"content":content}