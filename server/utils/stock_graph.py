import requests
import matplotlib.pyplot as plt
from io import BytesIO


def plot():
    api_key = '8CBCC47VNSZ62WIE'
    symbol = 'MSFT'

    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={api_key}'

    response = requests.get(url)
    data = response.json()['Time Series (Daily)']
    
    close_price = []
    time = []
    
    for date, values in data.items():
        time.append(date)
        close_price.append(float(values['4. close']))

    fig, ax = plt.subplots()
    ax.plot(time, close_price)
    ax.set_xlabel('Time')
    ax.set_ylabel('Close Price')
    ax.set_title('MSFT Close Price over Time')
    ax.tick_params(axis='x', rotation=45)
    plt.tight_layout()
    
    # Convert plot to PNG image
    img_buffer = BytesIO()
    fig.savefig(img_buffer, format='png')
    img_buffer.seek(0)
    
    # Return the image to the frontend
    return img_buffer.getvalue()
    

