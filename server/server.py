from flask import Flask,request,jsonify
import requests
from bs4 import BeautifulSoup
from flask_cors import CORS
from textblob import TextBlob
from nltk.corpus import brown
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from routes.news_routes import news_routes
from routes.news_content_routes import news_content_routes
from routes.extract_imp_keyword import extract_keyword_routes
from routes.extract_tweets import extract_tweets
# from routes.company_market_price import company_market_price_routes
from routes.stock_actual_plot import stock_actual_graph_route
import random
from urllib.parse import unquote
# import snscrape.modules.twitter as sntwitter

# from forms import RegistrationForm,LoginForm

# def extract_keywords(text):
#     tokens = word_tokenize(text)
#     stop_words = set(stopwords.words('english'))
#     keywords = [token.lower() for token in tokens if token.lower() not in stop_words]
#     return keywords

app=Flask(__name__)
CORS(app)

app.register_blueprint(news_routes)
app.register_blueprint(news_content_routes)
app.register_blueprint(extract_keyword_routes)
app.register_blueprint(extract_tweets)
app.register_blueprint(stock_actual_graph_route)

@app.route('/market_data', methods=['GET'])
def market_data():
   api_key = '8CBCC47VNSZ62WIE'
   market_prices=[]
   symbols = ['XAUUSD', 'XAGUSD','NSE' ]
   url = "https://www.nseindia.com/api/quote-equity?symbol=NIFTY%2050"
   headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299"}
   response = requests.get(url, headers=headers).json()
   print(response)
#    if 'data' in response and len(response['data']) > 0:
#     price = response['data'][0]['lastPrice']
#     else:
#     return {"error": "Unable to retrieve Nifty 50 price."}
#    market_prices.append({'Symbol': 'Nifty50', 'Price (INR)': price})
#    for symbol in symbols:
#     # url = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={symbol}&to_currency=INR&apikey={api_key}'
#     url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={api_key}'
#     response = requests.get(url).json()
#     latest_date = max(response['Time Series (Daily)'].keys())
#     print(symbol,'\n',response,'\n',"................................................................",'\n','\n')
#     # price = float(response['Time Series (Daily)'][latest_date]['4. close'])
#     exchange_rate_url = 'https://api.exchangeratesapi.io/latest?base=USD'
#     exchange_rate_response = requests.get(exchange_rate_url).json()
#     # exchange_rate = exchange_rate_response['rates']['INR']
#     # price_exch = round(price * 31.1035 * exchange_rate / 1000, 2)
#     # market_prices.append({'Symbol': symbol, 'Price (INR)': price})

   return {"marketPrice":market_prices}
   # Define the symbols for the financial instruments you want to retrieve data for
  

        




if __name__=="__main__":
    app.run(debug=True)