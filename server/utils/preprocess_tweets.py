import re
import string

def clean_tweet(tweet):
    tweet_text=tweet['text']
    # Remove URLs, RTs, and mentions
    tweet = re.sub(r"(?:\@|https?\://)\S+", "", tweet_text)
    tweet = re.sub(r"RT ", "", tweet_text)

    # Remove punctuation and convert to lowercase
    tweet = tweet.translate(str.maketrans("", "", string.punctuation))
    tweet = tweet.lower()

    # Remove extra spaces and return cleaned tweet
    tweet = re.sub(r"\s+", " ", tweet).strip()
    return tweet