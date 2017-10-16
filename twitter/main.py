import jsonRead
from KeywordStream import KeywordStream

if __name__ == '__main__':
    item = jsonRead.loadTrend()
    trends = item[1]
    myStream = KeywordStream(trends)
    myStream.on_start()
