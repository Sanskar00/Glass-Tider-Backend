# from newsapi import NewsApiClient
# import pandas as pd
# from dotenv import load_dotenv
# import os
# import json
# load_dotenv()
# def news_report(company_name):
#     news_api = os.environ.get('NEWS_API')
#     print(news_api)
#     company_name = json.loads(company_name)
#     company_name=company_name["word"]
#     newsapi = NewsApiClient(api_key=news_api)
#     articles = []
#     for i in range(1, 6):
#         news = newsapi.get_everything(q=company_name, page=i, language='en')
#         articles.extend(news['articles'])
    
#     df_news = pd.DataFrame(articles)
#     return df_news
