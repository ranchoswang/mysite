import json

def loadTrend():
    with open('/home/ubuntu/workspace/python/mysite/TwitterTag/items.json','r') as f:
        data = json.load(f)
    for record in data:
        for time in record['timeStamp']:
            print(float(time))
        for trend in record['tag']:
            print(trend.lstrip('#'))
        print("*****************")

loadTrend()
