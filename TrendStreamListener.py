from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import time
import sys

access_token = "762889126840377344-QokfOoxEdg30hhdhDrpTXSPZ1Xn3wlO"
access_token_secret = "Et0fFXrxcj3trVvvXKGbxDsqc9Ex6Wib6isIjJkgb61os"
consumer_key = "Gv4501GM9zTfFOmGxGB5lxUTU"
consumer_secret = "goZ5uM8yjZ9fki7iooh3lQj2HdBbrmzNKePCCmJfLPSmgxctBZ"


class TrendStreamListener(StreamListener):
    def on_data(self, raw_data):
        print(raw_data)
        return True

    def on_error(self, status_code):
        print(status_code)



if __name__ == "__main__":
    streamListener = TrendStreamListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token,access_token_secret)
    stream = Stream(auth, streamListener)
    sysBackup = sys.stdout
    startTime = time.time()
    f = open('python.txt','w')
    stream.filter(track=['python'], async=True)
    sys.stdout = f
    while True:
        endTime = time.time()
        if endTime - startTime > 60:
            break
    stream.disconnect()
    f.close()
    sys.stdout = sysBackup



