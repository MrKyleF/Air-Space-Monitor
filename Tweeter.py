#Kyle R Fogerty
#Tweeter: Tweets Locations
from twython import Twython
from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)
twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

#Uses temp_tweet.txt as data to tweet
def sendTweet():
    with open('temp_tweet.txt','r') as f:
        try:
            twitter.update_status(status=f.read())
            f.close()
        except:
            print("Error occurred tweeting:")
            f.close()
        else:
            f.close()



