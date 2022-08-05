import os
import random
import sys
import time

import tweepy

import credentials

# # from os import environ


CONSUMER_KEY = credentials.CONSUMER_KEY
CONSUMER_SECRET = credentials.CONSUMER_SECRET
ACCESS_KEY = credentials.ACCESS_KEY
ACCESS_SECRET = credentials.ACCESS_KEY_SECRET
#FORECAST_APIKEY = credentials.FORECAST_APIKEY

# use this when you've set the keys as environment variables later
# CONSUMER_KEY = environ['CONSUMER_KEY']
# CONSUMER_SECRET = environ['CONSUMER_SECRET']
# ACCESS_KEY = environ['ACCESS_KEY']
# ACCESS_SECRET = environ['ACCESS_SECRET']
# FORECAST_APIKEY = environ['FORECAST_APIKEY']


sys.path.append(os.path.abspath(os.path.join("..", "config")))


Ticker = 1


def tweet_lyric(filename):
    count = 0
    while True:
        with open(filename, encoding="utf8") as f:
            lines = f.readlines()
        for line in lines:
            count += 1
            rand_line = random.randint(0, len(lines) - 1)
            line = lines[rand_line]
            strings = ['Verse', 'Chorus', 'Interlude', 'Produced',
                       'Bridged', 'Intro', 'Outro']
            words = line.split()
            resultwords = [word for word in words if word.lower()
                           not in strings]
            if resultwords != "" and len(resultwords) > 10:
                # this will tweet a drake lyric every 30 minutes.
                auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
                auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
                api = tweepy.API(auth)
                tweet = line

                try:
                    api.update_status(tweet)
                    print('Tweeting a lyric...')
                    time.sleep(30)
                # Exception handeling
                except tweepy.TweepError as e:

                    # Print the root cause of the error
                    print(e.reason)
                    print('Lyric Tweet No.'+str(Ticker))
                    # Updating the ticker
                    Ticker = Ticker+1
                    time.sleep(30)


tweet_lyric('./data/drake_lyrics.txt')
