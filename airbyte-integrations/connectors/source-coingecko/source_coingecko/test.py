import json

res = json.loads('{"data":[{"timestamp":"2022-01-05T23:17:00.000000Z","hash":"loa3DCjClW2ZUbZNehtdWQuMB7y4ClUXUfTWgAtWl94","gateway":"11u4XLetGNzvkDDe15F74kWzK8Y2eFac1c6bLBtQhkdQzM8RxYp","block":1167694,"amount":183213,"account":"14Rqw67Er4T4mDitRR5hkvDbefXUhVQGiaVV4yzgSF3sVtu6PfU"},{"timestamp":"2022-01-05T21:47:54.000000Z","hash":"QtZxrKj-H_QN1_ZYv-087M5MiVW5x9tRnb09mx0mKF0","gateway":"11u4XLetGNzvkDDe15F74kWzK8Y2eFac1c6bLBtQhkdQzM8RxYp","block":1167596,"amount":1484653,"account":"14Rqw67Er4T4mDitRR5hkvDbefXUhVQGiaVV4yzgSF3sVtu6PfU"},{"timestamp":"2022-01-05T21:14:46.000000Z","hash":"BLo7uDqL1JUstoh-YZ9omIY1QFDfgf5ha3hSIiJRxWg","gateway":"11u4XLetGNzvkDDe15F74kWzK8Y2eFac1c6bLBtQhkdQzM8RxYp","block":1167563,"amount":411741,"account":"14Rqw67Er4T4mDitRR5hkvDbefXUhVQGiaVV4yzgSF3sVtu6PfU"},{"timestamp":"2022-01-05T14:07:16.000000Z","hash":"SKghbNhXWpS9KxSxpXoTIXnIHhzPr7AWa1AoKldkQyY","gateway":"11u4XLetGNzvkDDe15F74kWzK8Y2eFac1c6bLBtQhkdQzM8RxYp","block":1167099,"amount":314726,"account":"14Rqw67Er4T4mDitRR5hkvDbefXUhVQGiaVV4yzgSF3sVtu6PfU"},{"timestamp":"2022-01-05T11:24:21.000000Z","hash":"jYoy2xdwnUYWzH8YTKgBs7tudwto0P1ZNl4fTyI4rF4","gateway":"11u4XLetGNzvkDDe15F74kWzK8Y2eFac1c6bLBtQhkdQzM8RxYp","block":1166930,"amount":621238,"account":"14Rqw67Er4T4mDitRR5hkvDbefXUhVQGiaVV4yzgSF3sVtu6PfU"},{"timestamp":"2022-01-05T10:53:10.000000Z","hash":"-FZNBwc5wmBclsvYgOZCB3L5lYKm78Urt4BeCTOsGCc","gateway":"11u4XLetGNzvkDDe15F74kWzK8Y2eFac1c6bLBtQhkdQzM8RxYp","block":1166897,"amount":299236,"account":"14Rqw67Er4T4mDitRR5hkvDbefXUhVQGiaVV4yzgSF3sVtu6PfU"},{"timestamp":"2022-01-05T07:19:48.000000Z","hash":"1FMhMo5B7H-M-neE4-sKy0BDmGaVjNHN5ds1K7jGt1A","gateway":"11u4XLetGNzvkDDe15F74kWzK8Y2eFac1c6bLBtQhkdQzM8RxYp","block":1166672,"amount":1781653,"account":"14Rqw67Er4T4mDitRR5hkvDbefXUhVQGiaVV4yzgSF3sVtu6PfU"},{"timestamp":"2022-01-05T06:42:57.000000Z","hash":"dWNos4lItDdjOjbT7gf7FVH5dezqVvEruhIorimM_vw","gateway":"11u4XLetGNzvkDDe15F74kWzK8Y2eFac1c6bLBtQhkdQzM8RxYp","block":1166635,"amount":1251192,"account":"14Rqw67Er4T4mDitRR5hkvDbefXUhVQGiaVV4yzgSF3sVtu6PfU"},{"timestamp":"2022-01-05T00:36:25.000000Z","hash":"8oUR3gXzjBsI0wvHSbd1AS8kygpudgtRS8EAReEAp_A","gateway":"11u4XLetGNzvkDDe15F74kWzK8Y2eFac1c6bLBtQhkdQzM8RxYp","block":1166271,"amount":1517743,"account":"14Rqw67Er4T4mDitRR5hkvDbefXUhVQGiaVV4yzgSF3sVtu6PfU"}]}')

other = {"data":[]}

test = {"data":[{"timestamp":"2021-06-03T21:19:50.000000Z","hash":"infIoxCMOafeaELv4t5aztFSeRThcYhDzPXbBp0MmGQ","gateway":"11u4XLetGNzvkDDe15F74kWzK8Y2eFac1c6bLBtQhkdQzM8RxYp","block":869861,"amount":97207801,"account":"14Rqw67Er4T4mDitRR5hkvDbefXUhVQGiaVV4yzgSF3sVtu6PfU"},{"timestamp":"2021-06-03T20:19:10.000000Z","hash":"1bATKQbAWPwCRmZogb_M1lk66OcRBE9UFc1YMzn-Dfo","gateway":"11u4XLetGNzvkDDe15F74kWzK8Y2eFac1c6bLBtQhkdQzM8RxYp","block":869820,"amount":87425029,"account":"14Rqw67Er4T4mDitRR5hkvDbefXUhVQGiaVV4yzgSF3sVtu6PfU"},{"timestamp":"2021-06-03T18:21:27.000000Z","hash":"0nxvVZIDVdlLV9zZ9cQSW_3RyEbWAHQbQYIMzp7iwtQ","gateway":"11u4XLetGNzvkDDe15F74kWzK8Y2eFac1c6bLBtQhkdQzM8RxYp","block":869740,"amount":9090872,"account":"14Rqw67Er4T4mDitRR5hkvDbefXUhVQGiaVV4yzgSF3sVtu6PfU"},{"timestamp":"2021-06-03T12:17:08.000000Z","hash":"0AQDH-0KuglPQt1_Nq56QfZs7uikHV7iZJEPfTSY2eA","gateway":"11u4XLetGNzvkDDe15F74kWzK8Y2eFac1c6bLBtQhkdQzM8RxYp","block":869498,"amount":104686967,"account":"14Rqw67Er4T4mDitRR5hkvDbefXUhVQGiaVV4yzgSF3sVtu6PfU"},{"timestamp":"2021-06-03T07:47:26.000000Z","hash":"rB2XmqWW2N2uesQOOLL1a1R1sK0yBMYQrd0kRcVHknQ","gateway":"11u4XLetGNzvkDDe15F74kWzK8Y2eFac1c6bLBtQhkdQzM8RxYp","block":869260,"amount":9934122,"account":"14Rqw67Er4T4mDitRR5hkvDbefXUhVQGiaVV4yzgSF3sVtu6PfU"},{"timestamp":"2021-06-03T03:45:50.000000Z","hash":"8FM78s-ptw1yldiZr3nhiEhVOS2ru7KYLMYDHlvRxhI","gateway":"11u4XLetGNzvkDDe15F74kWzK8Y2eFac1c6bLBtQhkdQzM8RxYp","block":869025,"amount":98300733,"account":"14Rqw67Er4T4mDitRR5hkvDbefXUhVQGiaVV4yzgSF3sVtu6PfU"},{"timestamp":"2021-06-03T02:55:06.000000Z","hash":"mb2A0gEqZHDqKf_Fz7AmKRTAXYQDk-YDrqO9zMBEkhA","gateway":"11u4XLetGNzvkDDe15F74kWzK8Y2eFac1c6bLBtQhkdQzM8RxYp","block":868980,"amount":66,"account":"14Rqw67Er4T4mDitRR5hkvDbefXUhVQGiaVV4yzgSF3sVtu6PfU"},{"timestamp":"2021-06-03T23:02:06.000000Z","hash":"-WhIyo4nCLF66TZyfUE9dW6u1P4uxP7m66hTiw8FCUM","gateway":"11u4XLetGNzvkDDe15F74kWzK8Y2eFac1c6bLBtQhkdQzM8RxYp","block":869945,"amount":106892289,"account":"14Rqw67Er4T4mDitRR5hkvDbefXUhVQGiaVV4yzgSF3sVtu6PfU"}]}

def calculate_sum(data):
    sum = 0
    hashes = []
    for i  in data:
        if i["hash"] in hashes:
            continue
        hashes.append(i["hash"])
        sum += i["amount"]
    sum *= 1e-8
    return sum
print(calculate_sum(test['data']))
