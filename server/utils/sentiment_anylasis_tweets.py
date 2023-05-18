from textblob import TextBlob

def get_sentiment(tweet):
    analysis = TextBlob(tweet)
    return analysis.sentiment.polarity

