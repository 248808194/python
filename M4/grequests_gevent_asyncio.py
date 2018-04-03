from urllib import  request
import  gevent,time,asyncio,aiohttp
from gevent import  monkey
monkey.patch_all() #当前程序的所有io操作单独做上标记
from aiohttp import ClientSession
import requests
import threading,multiprocessing
old_time = time.time()


# def get_weather_all_result():
#         result = requests.get(url="http://180.153.238.109/123.html")  # params url post 参数
#         time.sleep(0.2)
#         print(result.status_code)
#
#         # city_aqi = a['results'][0]['air']['city']
#
# t_list = []
#
# for i in range(1024):
#     t = multiprocessing.Process(target=get_weather_all_result)
#     # t_list.append(t)
#     t.start()
#
# for i in range(1024):
#     get_weather_all_result()



























#
# async def hello():
#     async with ClientSession() as session:
#         async with session.get("http://180.153.238.109/123.html") as response:
#             print(response.status)
#             # response = await response.read()
#             # print(response)
#
#
#
# tasks = [hello for i in range(1000)]
# #print(tasks)
# loop = asyncio.get_event_loop()
# loop.run_until_complete(asyncio.wait([ii() for ii in tasks]))
# loop.close()

import json
import requests
import grequests


from urllib import request
import gevent
import gevent.monkey

# gevent.monkey.patch_socket()
gevent.monkey.patch_all()
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
print(len(all_city_name))
# all_city_name = all_city_name * 20
print(len(all_city_name))

all_city_name = all_city_name * 20

def crawler():
    def crawler_work(city_name):
        params = {
            'key': 'qdriqkdbyyqtwmis',
            'location': city_name,
            'language': 'zh-Hans',
            'unit': 'c'
        }
        print( u'start crawl {0}'.format(city_name))
        response = grequests.get("https://api.seniverse.com/v3/weather/now.json", params=params)
        print(response)
        print (u'end crawl {0}'.format(city_name))

    gevent_list = []
    for p in all_city_name:
        gevent_list.append(gevent.spawn(crawler_work, p))

    size = 100
    index = 0
    while index < len(gevent_list):
        gevent.joinall(gevent_list[index:index+size], timeout=120)
        index += size

if __name__ == '__main__':
    crawler()




print(time.time() - old_time)