from tweepy import API
from tweepy import OAuthHandler

access_token = "762889126840377344-RSHaopx13fsxKvlhoisxLYv8Tn9KYmm"
access_token_secret = "ZySzilmO9DMQCm01pOakr67XzioiOmuS0OWE8CaLuvYHF"
consumer_key = "PFgd0Uf6PT7EqU9L6viTy4ypx"
consumer_secret = "aORRR9IakCU2VR6kWu6Ep0e6XYlLIkAhXOSfsKSocP7xhp4y7b"


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


    def __repr__(self):
        def deEmpty(item):
            return item and item.strip()
        res = list(filter(deEmpty, self.trends))
        return res

    def insert_trend(self, data):
        for item in data:
            if item not in self.trends_set:
                if self.trends[self.index] in self.trends_set:
                    self.trends_set.remove(self.trends[self.index])
                self.trends[self.index] = item
                self.trends_set.add(item)
                self.index = (self.index + 1) % self.maxSize

    def get_raw(self):
        data = []
        trends_raw = self.trend_api.trends_place(self.us_WOE_ID)
        for item in trends_raw[0]['trends']:
            data.append(item)
        return data

    def update_trends(self):
        data = self.get_raw()
        self.insert_trend(data)
        return self.trends

    def updateTrend(self):
        return str(self.__repr__())

if __name__ == "__main__":
    trendLoader = TrendLoader()
    """
    if isinstance(trends[0]['trends'], list):
        print("trends[0]['trends'] is list")
        for item in trends[0]['trends']:
            print(item['name'])
    """
    demo_data1 = list(map(str, list(range(280))[:70]))
    demo_data2 = list(map(str, list(range(280))[70:140]))
    demo_data3 = list(map(str, list(range(280))[19:69]))
    demo_data4 = list(map(str, list(range(280))[200:270]))

    trendLoader.insert_trend(demo_data1)
    trendLoader.insert_trend(demo_data2)
    trends = trendLoader.updateTrend()
    trendLoader.insert_trend(demo_data3)
    trendLoader.insert_trend(demo_data4)

