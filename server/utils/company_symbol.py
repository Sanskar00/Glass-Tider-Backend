import requests
import json
from dotenv import load_dotenv
import os
load_dotenv()

# Define the company name
def compnay_symbol(company_name):
   
# Use yfinance to get the company's ticker symbol
  api_key = os.environ.get('ALPHA_API')
  # company_name = json.loads(company_name)
  # company_name=company_name["word"]
  # Construct the API request UR 
  url = f"https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={company_name}&apikey={api_key}"
  # Send the API reques
  response = requests.get(url)
  # Check if the request was successful and retrieve the stock symbo
  if response.status_code != 200:
    return "Could not retrieve stock symbol for company"
  else:
    results = response.json()["bestMatches"]
    if len(results) == 0:
        return("Error: Could not find company", company_name)
    else:
        symbol = results[0]["1. symbol"]
        return(symbol)


