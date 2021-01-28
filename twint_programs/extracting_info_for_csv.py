import tweepy
from tweepy import OAuthHandler

import csv
import json

from config import config_keys

print("Handling developer stuff!")

access_token = config_keys['access_token']
access_token_secret = config_keys['access_token_secret']
consumer_key = config_keys['consumer_key']
consumer_secret = config_keys['consumer_secret']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

try:
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    print("Done!")
except Exception as e:
    print("Error:" , e)

import pandas as pd
import numpy as np
from numpy.random import randint

csv_top_columns = ['geo', 'coordinates', 'place']
# entities_columns = ['hashtags', 'symbols', 'user_mentions', 'urls' ]
entities_columns = [ 'user_mentions', 'urls' ]
user_columns  = ['name', 'location', 'protected', 'created_at', 'time_zone', 'geo_enabled' ]

combined_columns = np.concatenate([ user_columns, csv_top_columns, entities_columns ])

df = pd.DataFrame(columns = combined_columns)

print("DataFrame Created!")
print(df)

query_string = "@Obs_IL"
query_count = 10
query_since = '2015-01-01'

count = 0
for tweet in tweepy.Cursor(api.search, q=query_string, count=query_count, since=query_since).items(query_count):
    print(count)
    # print("\n8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888\n")

    df.loc[count] = list(randint(10,size=(len(df.columns))))
    for i in tweet._json:

        if( str(i) == 'entities'):
            for k in entities_columns:
                df.loc[count][k] = str(tweet._json[i][k])
        
        elif( str(i) == 'user'):
            for k in user_columns:
                df.loc[count][k] = str(tweet._json[i][k])
        
        elif(i in csv_top_columns):
            df.loc[count][i] = str(tweet._json[i])

    count = count + 1

print("Dataframe generated of len: ", len(df))
df.to_csv(query_string+'.csv')

