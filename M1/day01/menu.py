#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date:2016-10-24-17-18
# Python 3.5

import  china_map
import login

def menu ():
    while True:
        print("-----------------")
        area_tmp = []
        for i in china_map.china_map.keys():#keys列表返回字典所有的key
            print(i)
            area_tmp.append(i)

        area = input("输入区域:")
        for a in range(len(area_tmp)):
            if area in area_tmp:
                provice_tmp = []
                for i  in (china_map.china_map.get(area).keys()):#get 返回指定键的值
                    provice_tmp.append(i)
                for i in provice_tmp:
                    print(i)
                provice = input("输入省份:")
                if provice in provice_tmp:
                    for i in (china_map.china_map.get(area).get(provice)):
                        print(i)
                    inp1 = input("Q:返回上一级/E:退出程序")
                    if inp1 == "Q":
                        continue
                    elif inp1 == "E":
                        login.main()

                break
            else:
                continue
