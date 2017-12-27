from pyspark import SparkContext
from pyspark.streaming import StreamingContext

from json import *


def myFilter(line):
    if line == "":
        return line
    data = loads(line)
    ans = {'created_at':data.pop('created_at'), 'id_str':data.pop('id_str'), 'text':data.pop('text')}
    #ans = {'Bob':data.pop('Bob'), 'Alice':data.pop('Alice')}
    return str(ans)


sc = SparkContext("local[2]", "Twitter_Filter")
ssc = StreamingContext(sc, 1)

lines = ssc.socketTextStream("localhost", 18288)


ans = lines.map(lambda line: myFilter(line)).filter(lambda line: line is not '')
ans.pprint()

ssc.start()
ssc.awaitTermination()

