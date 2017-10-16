import json

def loadTrend():
    with open('/home/ubuntu/workspace/python/mysite/TwitterTag/items.json','r') as f:
        data = json.load(f)
    timeStamp = []
    tag = []
    item = [timeStamp, tag]
    for record in data:
        time = record['timeStamp']
        for trend in record['tag']:
            timeStamp.append(time)
            tag.append(trend.lstrip('#'))
    return item


