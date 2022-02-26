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

def removeTxt(file_name):
    for i in range(0, len(file_name)):
        if file_name[i] == ".":
            return file_name[0:i]

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



