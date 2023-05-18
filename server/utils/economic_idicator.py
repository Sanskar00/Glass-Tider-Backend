import requests
import pandas as pd
from dotenv import load_dotenv
import os
load_dotenv()
def economic_idicator(symbol):
    api_key = os.environ.get('ALPHA_API')
    response = requests.get(f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={api_key}')
    data = response.json()
    df_econ = pd.DataFrame(data['Time Series (Daily)']).T
    df_econ.index = pd.to_datetime(df_econ.index)
    df_econ = df_econ[['4. close']]
    return df_econ
