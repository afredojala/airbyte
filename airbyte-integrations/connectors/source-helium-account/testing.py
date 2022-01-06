import json
from datetime import datetime, timedelta
with open('res.json', 'r') as f:
    data = json.load(f)

times = [datetime.fromtimestamp(d['record']["data"]['time']) for d in data]
times.sort()

i = 0
for x,y in zip(times[:-1], times[1:]):
    if y-x > timedelta(hours=6):
        print(f"before start: {times[i-1]}")
        print(f"start: {y}",f"end {x}")
        print(i)
    i = i+1
print(times[0], times[-1])