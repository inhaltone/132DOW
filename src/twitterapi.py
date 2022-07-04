import tweepy
from dotenv import load_dotenv
import os

load_dotenv()

auth = tweepy.OAuth1UserHandler(
    consumer_key=os.environ.get('API_KEY'),
    consumer_secret=os.environ.get('API_KEY_SECRET'),
    access_token=os.environ.get('ACCESS_TOKEN'),
    access_token_secret=os.environ.get('ACCESS_TOKEN_SECRET')
)


class TwitterApi:

    api = tweepy.API(auth)

    @staticmethod
    def getUserTimelineInit(user_id='@inhalt_'):
        """

        :param user_id:
        :type user_id: str
        """
        tweets_data = TwitterApi.api.user_timeline(screen_name=user_id,
                                                   count=200,
                                                   include_rts=True,
                                                   tweet_mode='extended'
                                                   )
        return tweets_data

    @staticmethod
    def getUserTimeline(username, oldest_id):
        """

        :param oldest_id:
        :type username: object
        """
        try:
            user_timeline = TwitterApi.api.user_timeline(screen_name=username,
                                                         count=200,
                                                         include_rts=True,
                                                         max_id=oldest_id - 1,
                                                         tweet_mode='extended'
                                                         )
        except:
            user_timeline = []
        return user_timeline

    @staticmethod
    def getQueryTweetsInit(query='#war'):
        """

        :type query: object
        """
        tweets_query = TwitterApi.api.search_tweets(q=query,
                                                    count=200,
                                                    lang="en",
                                                    until="2022-07-01"
                                                    )
        return tweets_query

    @staticmethod
    def getQueryTweets(query='#war', oldest_id=''):
        """

        :param query:
        :type oldest_id: object
        """
        try:
            tweets_query = TwitterApi.api.search_tweets(q=query,
                                                        count=100,
                                                        max_id=oldest_id - 1,
                                                        lang="en",
                                                        until="2022-07-01"
                                                        )
        except:
            tweets_query = []
        return tweets_query
