#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date:2016-11-10-14-10
# Python 3.5
#!/usr/bin/env python
#coding: utf-8
import json
import requests
import datetime

for i in  range(0,366):
    a= str(datetime.datetime.now()+datetime.timedelta(-i)).strip().split(" ")[0].strip().split("-") #时间格式转str
    time1 = a[0]+a[1]+a[2]
    print(time1)

    params = {
      'app' : 'weather.history',
      'appkey' : '10003',
      'weaid' : '101020100',
        'date' : time1,
      'sign' : 'b59bc3ef6191eb9f747dd4e83c99f2a4',
      'format' : 'json',
    }
    result = requests.get(params=params,url="http://api.k780.com:88") #params url post 参数
    # print(result)


    a = result.json()
    # print(a)
    json.dump(a,open("wather.json","w",encoding="utf8"),indent=4,ensure_ascii=False)
    b = a.get("result")

    day_aqi_his = []
    for i in b:
        day_aqi_his.append(int(i.get("aqi")))

    # print(day_aqi_his)
    tmp = 0
    for i in day_aqi_his:
        tmp += i
        day_aqi = int(tmp / len(day_aqi_his))
    print("当前日期:   %s    当天PM2.5:   %s"%(time1,day_aqi))