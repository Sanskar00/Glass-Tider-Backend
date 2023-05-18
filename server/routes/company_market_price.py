from flask import request,Blueprint,jsonify
from utils.extract_tweets import extractTweets
from utils.preprocess_tweets import clean_tweet
from utils.sentiment_anylasis_tweets import get_sentiment
from utils.company_symbol import compnay_symbol
from utils.economic_idicator import economic_idicator
from utils.news_report import news_report

import pandas as pd
import requests
import pandas as pd
import numpy as np
from dotenv import load_dotenv
import os
from yahooquery import Ticker
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.impute import SimpleImputer


company_market_price_routes=Blueprint('company_market_price',__name__)
@company_market_price_routes.route('/company_market_price',methods=['post'])
def compnay_market_price():
    word=request.data.decode('utf-8')
    symbol=compnay_symbol(word)
    df_econ=economic_idicator(symbol)
    df_news=news_report(word)
    api_key = os.environ.get('INT_API')
    print(symbol)

    
    company=Ticker(symbol)
    income_statement = company.income_statement()
    balance_sheet=company.balance_sheet()
    cash_flow = company.cash_flow()
    income_statement['dummy']='A'
    balance_sheet['dummy']='A'
    cash_flow['dummy']='A'

    df_econ = df_econ.reset_index().rename(columns={'index': 'date', '4. close': 'price'})
    df_news = df_news[['publishedAt', 'title']]



    # # Merge the dataframes
    df_merged = df_econ.merge(df_news, left_index=True, right_index=True)
    df_merged['dummy']='A'
    df_merged =pd.merge(income_statement, df_merged, on='dummy')
    df_merged =pd.merge(balance_sheet, df_merged, on='dummy')
    df_merged =pd.merge(income_statement, df_merged, on='dummy')
    

    df_merged['asOfDate']=pd.to_datetime(df_merged['asOfDate']).apply(lambda x: x.timestamp())
    df_merged['asOfDate_x']=pd.to_datetime(df_merged['asOfDate_x']).apply(lambda x: x.timestamp())
    df_merged['asOfDate_y']=pd.to_datetime(df_merged['asOfDate_y']).apply(lambda x: x.timestamp())
    df_merged['date']=pd.to_datetime(df_merged['date']).apply(lambda x: x.timestamp())
    df_merged = df_merged.drop('publishedAt', axis=1)
    df_merged = df_merged.dropna(axis=1)
    # df_merged=df_merged.drop('AllowanceForDoubtfulAccountsReceivable', axis=1)
    # df_merged = df_merged.drop('DefinedPensionBenefit', axis=1)
    # df_merged = df_merged.drop('EBITDA_x', axis=1)
    # df_merged = df_merged.drop('EBITDA_y', axis=1)
    # df_merged = df_merged.drop('GrossAccountsReceivable', axis=1)
    # df_merged = df_merged.drop('NonCurrentAccruedExpenses', axis=1)
    # df_merged = df_merged.drop('TradeandOtherPayablesNonCurrent', axis=1)
    df_merged = df_merged.drop('dummy', axis=1)
    df_merged = df_merged.drop('title', axis=1)
    df_merged = df_merged.drop('periodType', axis=1)
    df_merged = df_merged.drop('periodType_x', axis=1)
    df_merged = df_merged.drop('periodType_y', axis=1)
    df_merged = df_merged.drop('currencyCode', axis=1)
    df_merged = df_merged.drop('currencyCode_x', axis=1)
    df_merged = df_merged.drop('currencyCode_y', axis=1)  
    
    


    df_merged['price'] = df_merged['price'].astype(float)
    df_merged['price'] = pd.to_numeric(df_merged['price'], errors='coerce').fillna(0)

    nan_values = df_merged.isna()

    # print the DataFrame with NaN values highlighted
    print(df_merged.style.highlight_null(null_color='red'))
    # print(df_merged.isinf())


    # df_merged=df_merged.dropna()
    # print(df_merged['price'])
    if df_merged['price'].notna().all():
        print('Column A does not have empty cells')
    else:
        print('Column A has empty cells')
    
    df_dict = df_merged.to_dict(orient='records')

    X = df_merged.drop('price', axis=1).values
    y = df_merged['price'].values
    print(df_merged['price'])

    # # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    imputer = SimpleImputer(strategy='mean')

    imputer.fit(X_train)

    X_train = imputer.transform(X_train)
    X_test = imputer.transform(X_test)

    lr = LinearRegression()
    lr.fit(X_train, y_train)

    y_pred = lr.predict(X_test)
    print(y_pred)
    mse = mean_squared_error(y_test, y_pred)
    print('Mean squared error:', mse)
    return jsonify({'df_merged':df_dict })

    


 # tweets=extractTweets(word)
    # df_tweets=pd.DataFrame(tweets,columns=['tweets'])
    # df_tweets['clean_tweet'] = df_tweets['tweets'].apply(clean_tweet)
    # df_tweets['sentiment'] = df_tweets['clean_tweet'].apply(get_sentiment)
