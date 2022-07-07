import praw
import pandas as pd
from authenticate import redditAuthenticate

reddit = redditAuthenticate()

posts = []
comments = []
nlp_subreddit = reddit.subreddit('nba')
for post in nlp_subreddit.hot(limit=10): #hot, rising, popular etc tags
    posts.append([post.title, post.url])

posts = pd.DataFrame(posts, columns=['title', 'url'])
posts.to_csv('nlp8.csv')