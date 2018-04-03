#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date:2017-03-30-16:20
# Python 3.5
import asyncio,time
from aiohttp import ClientSession

all_city_name = [
'Hanjiang',
'Yangzhou',
'Tianchang',
'Mengzhou',
'Jiyuan',
'Wenxian',
'Qinyang',
'Xinmi',
'Xingyang',
'Zhengzhou',
'Shangjie',
'Wuzhi',
'Linying',
'Yanling',
'Xihua',
'Fugou',
'Weishi',
'Taikang',
'Zhecheng',
'Suixian',
'Zhongmou',
'Tongxu',
'Kaifeng',
'Yuanyang',
'Yanjin',
'Fengqiu',
'Minquan',
'Lankao',
'Zezhou',
'Boai',
'Jincheng',
'Gaoping',
'Jiaozuo',
'Xiuwu',
'Huojia',
'Xinxiang',
'Huixian',
'Lingchuan'
    ]
all_city_name = all_city_name * 20

old_time = time.time()
async def hello(city_name):
    params = {
            'key': 'qdriqkdbyyqtwmis',
            'location':city_name,
            'language':'zh-Hans',
            'unit':'c'
        }
    async with ClientSession() as session:
        # async with session.get("https://api.seniverse.com/v3/weather/now.json",params=params) as response:
        async with session.get("http://180.153.238.109/") as response:
            response = await response.read()
            a = response
            print(eval(a.decode()))


loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait([hello(x) for x in all_city_name]))
loop.close()
print(time.time() - old_time)