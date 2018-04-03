#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date:2017-03-29-15:25
# Python 3.5

#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date:2017-02-10-16:11
# Python 3.5

# property 是将一个方法变成一个属性
# 如果需要写则需要加上setter
import time,requests,json,re,threading
import gevent
from gevent import monkey
monkey.patch_all(httplib=True)

class Check_Weather(object):
    def __init__(self,city_name):
        self.params = {
            'key': 'qdriqkdbyyqtwmis',
            'location':city_name,
            'language':'zh-Hans',
            'unit':'c'
        }

    def get_weather_all_result(self):
        try:
            result = requests.get(params=self.params, url="https://api.seniverse.com/v3/air/now.json")  # params url post 参数
            a = result.json()
            city_aqi = a['results'][0]['air']['city']
            return city_aqi
        except Exception as e:
            print(e)


    # @property
    def get_pm(self): # 默认查询上海天气/也可以更具当前的地理位置查询当前所在的天气
        get_result = self.get_weather_all_result()
        print ('current city now pm2.5 is ',self.params['location'],get_result['pm25']) # 返回当天的天气值

city_name = [
'Hanjiang',
 'Yangzhou',
 'Tianchang',
 'Jinhu',
 'Gaoyou',
 'Sihong',
 'Siyang',
 'Hongze',
 'Baoying',
 'Huaian',
 'Huaiyinqu',
 'Huaianqu',
 'Jiangdu',
 'Taizhou',
 'Jiangyan',
 'Xinghua',
 'Rugao',
 'Haian',
 'Dongtai',
 'Yandu',
 'Yancheng',
 'Jianhu',
 'Dafeng',
 'Songjiang',
 'Qingpu',
 'Minhang',
 'Xujiahui',
 'Shanghai',
 'Pudong',
 'Xuchang',
 'Yuzhou',
 'Changge',
 'Xinzheng',
 'Yanshi',
 'Dengfeng',
 'Gongyi',
 'Jili',
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
 'Lingchuan' ]
# a = Check_Weather('huojia')
# a.get_pm()

asdf = time.time()
#
gevent_list = []
for i in city_name:
    a = Check_Weather(i).get_pm
    gevent_list.append(gevent.spawn(a))
gevent.joinall(gevent_list)


print('excuting all time is ',time.time()  -asdf )
print(123)