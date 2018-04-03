#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date:2016-11-03-09-36
# Python 3.5


# def print_single_tuple(*args):
#     print(args,type(args))
#     for a,b in enumerate(args):
#         print(" %s  is %s"%(a,b))
#
#
#
# print_single_tuple(tuple("zhoutao"))


"""
json 数据格式
{"phone": {"motoxpro": [2800, 10],"sonyp1": [1800, 30]}}
额外 *1：将列表中的数字从大到小排列
extend append 区别
    extend 为列表中追加一个可迭代的对象
    append 为列表中追加一个元素
1:zip函数
2：enumerate函数
3:将商品第一个字符串大写
4：统计o，在所有商品中出现的次数
5：检查那个商品是以pro结尾的
6：判断iphone6至少有一个字符
7：商品名称字符串分割成单个字符，用 | 分割开
8：将商品名称全部转换成大写
9：将商品名称全部转换为小写
10：将商品名称中的空格去除掉
11:检查那个商品以p开头，(此处忽略大小写)
12:将商品名第一个字母大写
13：将motoxpro 替换成moto z
14:将moto z 修改成moTo z
15:添加 商品huawei P9，单价1500，数量22台 到json中去，
16：讲motoxpro 商品下架
17：打印出iphone6的单价
18：计算出iphone6 比 huawei p9 贵多少钱
19：列出全部商品名，
20：打印库存中所有总价
21：在iphone6 前面插入 not sale
22：删除iphone6 not sale字段
23：将 品名，单价，数量，全部放到一个大列表中去example [["motoxpro",2500,10],["sonyp1","1500","20"].....]
24:将品名，单价，数量，全部放到一个大元祖中去中去example (["motoxpro",2500,10],["sonyp1","1500","20"].....)
25:比较iphone6 和motox 那个贵
26：创建motoxpro2 当motoxpro单价 或 数量修改时候 motoxpro2也随之改变
27：用元祖列表，列表元祖，dict_fromkeys ,{},dict()创建原json格式
28：访问json数据中字典的值
29：讲motoxpro 的 数量修改为10，单价调整为1200
30：浅复制原来的json数据。创建零时字典tmp_json
31：打印出motoxpro中的单价以及数量
31：打印出全部商品的单价以及数量
32：删除motoxpro 这个商品
33：将json数据转换为字典 ，键值队输出为元祖类型，并且修改iphone6的价格为1500
###集合

"""
# import json
# dict_json = json.load(open("test.json","r"))
# print(dict_json)
#
# for i in dict_json:
#     print("%s\t\t\t 当前价格%s\t\t\t\t 库存数量%s"%(i,dict_json[i][0],dict_json[i][1])) # 打印商品单价，库存 型号


#3 将商品首字母设成大写,并且写入到文件中去
#字典key 无法修改，修改新建一个字典从新写入到文件中去
import json
import string
# dict_json = json.load(open("test.json","r"))
# a={}
# for i in dict_json.keys():
#     a[i.capitalize()] = (dict_json.get(i))
# print(a)
#
# json.dump(a,open("test.json",'w'))
#
# # q4,q5
#
# q4=""
# for i in a.keys():
#     q4 += i  # 将获取到keys 后将字符串分别相加
#     print("|".join(i)) # q 7
#     print(i.upper())
#     if i.endswith("pro"):
#         print("商品 %s 以pro结尾"%i)
#     else:
#         continue
# print("字母 “o”，在所有商品名称中一共出现 %s" %(q4.count("o") ) )


# 将motoxpro 换成moto z
# 创建moto z 在删除motoxpro
dict_a=json.load(open("test.json","r"))
# dict_a.setdefault("moto x",dict_a.pop("Motoxpro")) # pop 删除并返回键值
print(dict_a,type(dict_a))
#
# dict_a.setdefault("huawei p9",[1500,22]) #添加huawei p9 到json中去
#
# json.dump(dict_a,open("test.json","w"))
#
# # 将moto x 商品下架
# # dict_b = json.load(open("test.json","r"))
# # dict_b.pop("moto x")
# # json.dump(dict_b,open("test.json","w"))
#
# dict_c = json.load(open("test.json","r"))
# single_iphone_price = dict_c.get("Iphone6")[0] #打印出iphone6 的价格
# print(single_iphone_price)
#
# single_p9_price = dict_c.get("huawei p9")[0] #dict.get(keyname) 获得keyname value
#
# iphone_p9 = int(single_iphone_price) - int(single_p9_price)
#
# print(iphone_p9)

#
#
# #20：打印库存中所有总价
# sum_all_price = []
# dict_d = json.load(open("test.json","r"))
# for i in dict_d.values():
#     sum_all_price.append(int(i[0]) * int(i[1]) )
# a=0
# for i in sum_all_price:
#    a+=i
#
# print(a)
#
# # 将json数据转换为字典 ，键值队输出为元祖类型，并且修改iphone6的价格为1500
#
# dict_f = json.load(open("test.json","r"))
# # print(dict_f)
#
# for i in dict_f.keys():
#     # print(i)
#     tmp_tuple = (tuple( dict_f.get(i) ))
#     dict_f[i] = tmp_tuple
# print(dict_f)
#
# json.dump(dict_f,open("test1.json","w"))
#
# a = json.load(open("test1.json","r"))
# print(a)
# print(type(a.get("Iphone6")))