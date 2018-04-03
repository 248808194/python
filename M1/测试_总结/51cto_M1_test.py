#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date:2016-11-07-10-27
# Python 3.5

import string
import json
"""

s1,18,aaa,linux
s2,38,bbb,python
teacher,16,alex
读取文件，输出为json格式
"""

with open("01todo","r") as file:
    stu_list = [] #定义学生列表
    tech_dict = {}
    for i in file:
        i = i.strip().split(",") #分割成列表
        if len(i) == 4: #判断如果长度为4，则放到学生列表中去
            stu_list.append( {i[0]:{"age":i[1],"name":i[2],"study":i[3]}} )
        else:
            tech_dict.setdefault(i[0],{i[1]:i[2]}) #如果长度不为4，则生成老师字典
    all_dict = {"student":stu_list}  #定义all_dict 字典先将 学生添加进去
    all_dict.update(tech_dict) #在更新字典将老师写进去

json.dump(all_dict,open("t.json","w",),indent=1) #将字典文件通过json dump写入到t.json文件中去



with open("01todo", "r") as file:
    all_dict = {}
    list_stu = []
    for i in file:
        if i.startswith("s"):
            i = i.strip().split(",")
            list_stu.append(dict ([( i[0] ,dict([("age",i[1]),("name",i[2]),("study",i[3])]) )])) #下面这种方法利用字典的工厂函数dict() 比较难于阅读
            all_dict.update(dict([("student", list_stu)]))
        else:
            i = i.strip().split(",")
            all_dict.update(dict([(i[0], dict([("age", i[1]), ("name", i[2])]))]) )
            # print(all_dict)

json.dump(all_dict,open(".json","w"), indent=1)

