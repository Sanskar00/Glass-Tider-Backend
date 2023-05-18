import requests
import pandas as pd
from datetime import datetime,timedelta

def company_his_df(symbol):
    api_key = '8CBCC47VNSZ62WIE'
    print(symbol)
    ten_years_ago = (datetime.today() - timedelta(days=730)).strftime('%Y-%m-%d')
    today = datetime.today().strftime('%Y-%m-%d')
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={api_key}&outputsize=full'

    response = requests.get(url)
    data = response.json()['Time Series (Daily)']

    df_list = []
    for date, values in data.items():
         if date >= ten_years_ago and date <= today:
            open_price = values['1. open']
            high_price = values['2. high']
            low_price = values['3. low']
            close_price = values['4. close']
            adjusted_close_price = values['5. adjusted close']
            volume = values['6. volume']
            date_obj = datetime.strptime(date, "%Y-%m-%d")
            date = date_obj.strftime("%-m/%-d/%Y")
            df_list.append(pd.DataFrame({
                'Date': date,
                'Open': open_price,
                'High': high_price,
                'Low': low_price,
                'Close': close_price,
                'Adj Close': adjusted_close_price,
                'Volume': volume
            }, index=[0]))

    df = pd.concat(df_list, ignore_index=True)
    return df