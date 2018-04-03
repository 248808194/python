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
monkey.patch_all()

class Check_Weather(object):
    today_time = time.strftime("%Y%m%d", time.localtime())
    def __init__(self,city_name):
        # self.weaid = weaid # 城市ＩＤ
        self.params = {
            'key': 'qdriqkdbyyqtwmis',
            'location':city_name,
            'language':'zh-Hans',
            'unit':'c'
            # 'appkey': '10003',
            # 'weaid': self.weaid, #bj:101010100 ,sh:101020100
            # 'date': self.today_time,
            # 'sign': 'b59bc3ef6191eb9f747dd4e83c99f2a4',
            # 'format': 'json',

        }

    def get_weather_all_result(self):
        result = requests.get(params=self.params, url="https://api.seniverse.com/v3/air/now.json")  # params url post 参数
        # print(result,type(result))
        a = result.json()
        city_aqi = a['results'][0]['air']['city']

        # json.dump(a, open("wather.json", "w", encoding="utf8"), indent=4, ensure_ascii=False)
        return city_aqi


    # @property
    def get_pm(self): # 默认查询上海天气/也可以更具当前的地理位置查询当前所在的天气
        get_result = self.get_weather_all_result()
        print (get_result['pm25']) # 返回当天的天气值

    # @get_pm.setter
    # def get_pm(self,newcity): # 自定义天气查询
    #     self.params['location'] = newcity
    #     self.get_pm
    #
    # @property
    # def get_wind(self):
    #     # get_wind_dict = {}
    #     get_result = self.get_weather_all_result()
    #     for k,v in get_result.items():
    #         if re.findall('wind*',k):
    #             print('%s is %s'%(k,v))
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
 'Kunshan',
 'Taicang',
 'Jiading',
 'Baoshan',
 'Chongming',
 'Pudongnanhui',
 'Haimen',
 'Tongzhou',
 'Rudong',
 'Qidong',
 'Shilong',
 'Pingdingshan',
 'Baofeng',
 'Ruzhou',
 'Xiangcheng',
 'Jiaxian',
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
 'Qixian',
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
# city_name = ['huixian','Lingchuan']
gevent_list = []


# Check_Weather('huixian').get_pm()

for i in city_name:
    a = Check_Weather(i).get_pm
    gevent_list.append(gevent.spawn(a))
#     # print(single_city_get_pm)
#     # gevent_list.append(single_city_get_pm)



# print(gevent_list)
gevent.joinall(gevent_list)





# city_weather = Check_Weather(101020100)
# func = getattr(city_weather,'get_pm')
# func
# func = setattr(city_weather,'get_pm','101010100') #
# func
# # 用反射的时候注释掉property
# def main():
#     cityid = input("请输入城市代码:")
#     city_weather = Check_Weather(cityid)
#
#     inp = input("enter detail to see such as pm/wind/temp.....")
#     if hasattr(city_weather,inp):
#         func = getattr(city_weather,inp)
#         func()
#     else:
#         print('method not found try again')
#
#
# if __name__ == '__main__':
#     main()