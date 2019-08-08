import tweepy
import textblob
import json

def get_tweets_with_keyword(consumer_key,consumer_secret,access_token,access_token_secret,query,count):
    consumer_key = consumer_key
    consumer_secret = consumer_secret
    access_token = access_token
    access_token_secret = access_token_secret
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    try:
        search_results = api.search(q=query, count=count)
        return [t.text for t in search_results]
    except tweepy.error.TweepError as x:
        print("There is an exception: " + x.response.text)
    except:
        print("There is a problem:")


def twitter_sentiment_analyzser(tweets):
    avg_polarity=0
    avg_subjectivity=0
    sentiment_assessments=[]
    for t in tweets:
        tb=textblob.TextBlob(t)
        avg_polarity+=tb.sentiment.polarity
        avg_subjectivity+=tb.sentiment.subjectivity
       # sentiment_assessments.append(tb.sentiment_assessments)
    return ((avg_polarity/len(tweets)),(avg_subjectivity/len(tweets)))