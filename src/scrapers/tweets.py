import pandas as pd
from prototypes.endpoints import Hashtags
from prototypes.twitterapi import TwitterApi


twitter_df = pd.DataFrame()
all_tweets = []
username = '@UkrWarReport'
query_string = Hashtags.PUTIN_WAR_CRIMINAL.value
# tweets = getUserTimelineInit(username)
tweets = TwitterApi.getQueryTweetsInit(query_string)
all_tweets.extend(tweets)
oldest_id = tweets[-1].id

while True:
    data_list = []
    # tweets = getUserTimeline()
    tweets = TwitterApi.getQueryTweets(query_string, oldest_id)
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
twitter_df.to_csv('data/raw/tweets/hash-putin-war-criminal.tsv', sep='\t')
