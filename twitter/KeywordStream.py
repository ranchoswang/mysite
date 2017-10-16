from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream


access_token = "762889126840377344-QokfOoxEdg30hhdhDrpTXSPZ1Xn3wlO"
access_token_secret = "Et0fFXrxcj3trVvvXKGbxDsqc9Ex6Wib6isIjJkgb61os"
consumer_key = "yPeGer40a7aDrkFuYDvaVShSZ"
consumer_secret = "oa2uHG9hNQ3sqBv1uIVLfTROKJyXUzJyAbB0atTWKIamYr0ctK"

class KeywordListener(StreamListener):

    def on_data(self, raw_data):
        print(raw_data)
        return True

    def on_error(self, status_code):
        print(status_code)


class KeywordStream:
    def __init__(self, keyword):
        self.keyword = keyword
    def on_start(self):
        listener = KeywordListener()
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        stream = Stream(auth, listener)
        stream.filter(track=self.keyword)
