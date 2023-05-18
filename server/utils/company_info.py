import requests

def company_info(symbol):
        # Make a request to the Alpha Vantage API
    response = requests.get('https://www.alphavantage.co/query', params={
        'function': 'GLOBAL_QUOTE',
        'symbol': symbol,
        'apikey': '8CBCC47VNSZ62WIE'
    })

    # Parse the JSON response
    data = response.json()
    print(data)

    company_info={}

    # Extract the close price, volume, and change percentage
    open_price=float(data['Global Quote']['02. open'])
    high=float(data['Global Quote']['03. high'])
    low=float(data['Global Quote']['04. low'])
    close_price = float(data['Global Quote']['05. price'])
    previous_close=float(data['Global Quote']['08. previous close'])
    volume = int(data['Global Quote']['06. volume'])
    change=float(data['Global Quote']['09. change'])
    change_percent = float(data['Global Quote']['10. change percent'].rstrip('%'))

    company_info['open_price']=open_price
    company_info['high']=high
    company_info['low']=low
    company_info['close_price']=close_price
    company_info['previous_close']=previous_close
    company_info['volume']=volume
    company_info['change']=change
    company_info['change_percent']=change_percent

    return company_info


