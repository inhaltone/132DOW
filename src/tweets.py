import tweepy
from dotenv import load_dotenv
import os
import pandas as pd
from endpoints import Hashtags

load_dotenv()

auth = tweepy.OAuth1UserHandler(
    consumer_key=os.environ.get('API_KEY'),
    consumer_secret=os.environ.get('API_KEY_SECRET'),
    access_token=os.environ.get('ACCESS_TOKEN'),
    access_token_secret=os.environ.get('ACCESS_TOKEN_SECRET')
)

api = tweepy.API(auth)


def getUserTimelineInit(user_id='@inhalt_'):
    """

    :param user_id:
    :type user_id: str
    """
    tweets_data = api.user_timeline(screen_name=user_id,
                                    count=200,
                                    include_rts=True,
                                    tweet_mode='extended'
                                    )
    return tweets_data


def getUserTimeline():
    user_timeline = api.user_timeline(screen_name=username,
                                      count=200,
                                      include_rts=True,
                                      max_id=oldest_id - 1,
                                      tweet_mode='extended'
                                      )
    return user_timeline


def getQueryTweetsInit(query='#war'):
    tweets_query = api.search_tweets(q=query,
                                     count=200,
                                     lang="en",
                                     until="2022-07-01"
                                     )
    return tweets_query


def getQueryTweets(query='#war'):
    try:
        tweets_query = api.search_tweets(q=query,
                                         count=100,
                                         max_id=oldest_id - 1,
                                         lang="en",
                                         until="2022-07-01"
                                         )
    except:
        tweets_query = []
    return tweets_query


twitter_df = pd.DataFrame()
all_tweets = []
username = '@UkrWarReport'
query_string = Hashtags.UKRAINE_RUSSIA_WAR.value
# tweets = getUserTimelineInit(username)
tweets = getQueryTweetsInit(query_string)
all_tweets.extend(tweets)
oldest_id = tweets[-1].id

while True:
    data_list = []
    # tweets = getUserTimeline()
    tweets = getQueryTweets(query_string)
    print("TWEETS COUNT:", len(tweets), "=== from: ", query_string)
    if len(tweets) == 0:
        break

    for tweet in tweets:
        data = {
            'created_at': tweet.created_at,
            # 'full_text': tweet.full_text,
            'full_text': tweet.text,
            'favorite_count': tweet.favorite_count,
            'retweet_count': tweet.retweet_count,
            # 'account_name': username,
            'account_name': tweet.user.name,
            'id': tweet.id
        }
        data_list.append(data)
    oldest_id = tweets[-1].id
    all_tweets.extend(tweets)
    twitter_df = pd.concat([twitter_df, pd.DataFrame(data_list)], axis=0, ignore_index=True)
    print('N of tweets downloaded till now {}'.format(len(all_tweets)))

print('finished')
twitter_df.to_csv('data/tweets/hash-ukraine-russia-war.tsv', sep='\t')
