from datetime import datetime, timedelta
import time
import json
from typing import Dict
import requests

def find_earliest(account:str):
    if account == "12yZTfnLdiKZmHQDBcGqJP3go1QXkibYsZhhfuxdgqyNyqdr22j":
        start_date = datetime.strptime("2021-06-05T00:00:00", "%Y-%m-%dT%H:%M:%S")
        return
    elif account == "14g9NkZjzgs1BxNj4bp3dgM8bt6aQQoqgMG3xHUmJcKqe3enu74":
        start_date = datetime.strptime("2021-06-24T00:00:00", "%Y-%m-%dT%H:%M:%S")
        return
    elif account == "14Rqw67Er4T4mDitRR5hkvDbefXUhVQGiaVV4yzgSF3sVtu6PfU":
        start_date = datetime.strptime("2021-01-01T00:00:00", "%Y-%m-%dT%H:%M:%S")
        
    elif account == "12wq1a8TjZrUm9hj6ap3PiNF8z3XTYfNcjJvdAjUL5oEEsY5jsH":
        start_date = datetime.strptime("2021-08-01T00:00:00", "%Y-%m-%dT%H:%M:%S")
    else:
        start_date = datetime.strptime("2020-08-01T00:00:00", "%Y-%m-%dT%H:%M:%S")
    interval = timedelta(days=1)
    while start_date < datetime.now():
        params = {
            'min_time' : start_date.strftime("%Y-%m-%dT%H:%M:%S"),
            'max_time' : (start_date+interval).strftime("%Y-%m-%dT%H:%M:%S")
        }
        start_date += interval
        url = f"https://api.helium.io/v1/accounts/{account}/activity"
        res = fetch(url, params.copy())
        if res:
            print(account)
            min_time = int(datetime.now().timestamp()*2)
            for t in res:
                if t["time"] < min_time:
                    min_time = t["time"]
            print(datetime.fromtimestamp(min_time))
            print(datetime.fromtimestamp(res[-1]["time"]))
            break

        time.sleep(1)
        

def fetch(addr, params: Dict):
    results = []
    res = requests.get(addr,params=params)
    if res.status_code != 200:
        print(res)
    res = res.json()
    results.extend(res["data"])
    if 'cursor' in res.keys():
        params.update({'cursor' : res["cursor"]})
        res = requests.get(addr,params=params).json()
        results.extend(res["data"])
    # while res["cursor"]:
    #     params.update({'cursor' : res["cursor"]})
    #     res = requests.get(addr,params=params).json()
    #     if not res["data"]:
    #         break
    #     results.extend(res["data"])
    return results

galiot_accs = ['12yZTfnLdiKZmHQDBcGqJP3go1QXkibYsZhhfuxdgqyNyqdr22j', \
              '14g9NkZjzgs1BxNj4bp3dgM8bt6aQQoqgMG3xHUmJcKqe3enu74', \
              '14Rqw67Er4T4mDitRR5hkvDbefXUhVQGiaVV4yzgSF3sVtu6PfU', \
              '12wq1a8TjZrUm9hj6ap3PiNF8z3XTYfNcjJvdAjUL5oEEsY5jsH', \
              '14i7jbMoo8Tpq6MUDKmgZJnGmnzgnsyptPmfeV5fnbVNNcBDTwy']
for account in galiot_accs:
    find_earliest(account=account)