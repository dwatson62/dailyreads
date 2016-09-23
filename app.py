from __future__ import absolute_import, print_function
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import os
import json
import settings

consumer_key = os.getenv("TWITTER_CONSUMER_KEY")
consumer_secret = os.getenv("TWITTER_CONSUMER_SECRET")
access_token = os.getenv("TWITTER_ACCESS_TOKEN")
access_token_secret = os.getenv("TWITTER_ACCESS_SECRET")

class LikedTweetsListener(StreamListener):
  def on_data(self, data):
    tweet = json.loads(data)
    if 'event' in tweet and tweet['event'] == 'favorite':
      print(tweet)
    return True

  def on_error(self, status):
    print("Error status received  {0}".format(status))

if __name__ == '__main__':
  l = LikedTweetsListener()
  auth = OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_token, access_token_secret)

  stream = Stream(auth, l)
  stream.userstream()
