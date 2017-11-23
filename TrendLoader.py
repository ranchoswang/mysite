from tweepy import API
from tweepy import OAuthHandler

access_token = "762889126840377344-QokfOoxEdg30hhdhDrpTXSPZ1Xn3wlO"
access_token_secret = "Et0fFXrxcj3trVvvXKGbxDsqc9Ex6Wib6isIjJkgb61os"
consumer_key = "Gv4501GM9zTfFOmGxGB5lxUTU"
consumer_secret = "goZ5uM8yjZ9fki7iooh3lQj2HdBbrmzNKePCCmJfLPSmgxctBZ"


class TrendLoader():
    def __init__(self):
        self.us_WOE_ID = 23424977
        self.trends = []
        self.maxSize = 120
        self.index = 0
        self.trends_set = set([])
        for i in range(self.maxSize):
            self.trends.append('')

        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        self.trend_api = API(auth_handler=auth)

    def insert_trend(self, data):
        for item in data:
            if item not in self.trends_set:
                pass


    def get_raw(self):
        data = []
        trends = self.trend_api.trends_place(self.us_WOE_ID)
        for item in trends[0]['trends']:
            data.append(item)
        return data

    def update_trends(self):
        data = self.get_raw()
        self.insert_trend(data)
        return self.trends

if __name__ == "__main__":
    trendLoader = TrendLoader()
    """
    if isinstance(trends[0]['trends'], list):
        print("trends[0]['trends'] is list")
        for item in trends[0]['trends']:
            print(item['name'])
    """
    demo_data1 = str(range(70))