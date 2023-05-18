import os
import json
import praw
import datetime
def extractTweets(word):
    client_id = os.environ.get('REDDIT_CLIENT_ID')
    client_secret=os.environ.get('REDDIT_CLIENT_SECRET')
    user_agent="Scrapper 1.0 by /u/North_Key2066"
    reddit=praw.Reddit(
        client_id=client_id,
        client_secret=client_secret,
        user_agent=user_agent
    )
    sub='india' 
    sort = "latest" 
    limit = 50
    top_posts = reddit.subreddit(sub).search(word, sort=sort, limit=limit)
    total_posts=list()

    for post in top_posts:
        title=post.title
        score=post.score
        subreddit=sub
        number_of_comments=post.num_comments
        publish_date=datetime.datetime.utcfromtimestamp(post.created).strftime('%d %B %Y')
        author=post.author.name
        data_set={"title":title,"score":score,"number_of_comments":number_of_comments,"publish_date":publish_date,"author":author, "subreddit":sub}
        total_posts.append(data_set)
    
    return total_posts
    







    