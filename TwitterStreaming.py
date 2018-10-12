#install tweepy using: pip install tweepy

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
#Ayesha: always import json library
import json

# you need to create your api key from twitter developer portal
#consumer key, consumer secret, access token, access secret. UPDATE THESE TO THE ONES YOU OBTAIN.
ckey="fsdfasdfsafsffa"
csecret="asdfsadfsadfsadf"
atoken="asdf-aassdfs"
asecret="asdfsadfsdafsdafs"

#Ayesha: replace above with consumer_key, consumer_seceret, access_token, access_token_secret

#this class will be used to collect tweets
class listener(StreamListener):

    def on_data(self, data):
        # do stuff with the tweets. write to file, to db, etc
        #Ayesha: print just the tweets and save with below 4 lines of code and comment out line 28
        tweet = json.loads(data)
        tweet["text"]
        with open("kanyeWest.txt","a") as outFile:
            outFile.write(data + "\n")
        #print(data)
        return(True)

    def on_error(self, status):
        print(status)

# authorize 
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

#start stream
twitterStream = Stream(auth, listener())
twitterStream.filter(track=["kanye west"])

#Ayesha: fill in where kanye west is to search on Twitter

#Ayesha: type python ./TwitterStreaming.py in shell to produce json file for tweets
