#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date:2016-12-23-14:38
# Python 3.5

# 遍历循环字典，首先满足where的条件，先将满足ｗｈｅｒｅ条件的参数拿出来，拿出来的应该是一个ｄｉｃｔ　，在将ｓｅｌｅｃｔ需要查询的字段打印出来
# 将where_part_list 0,2 参数，代入到
import re


def dayu(old_dict,select_part_list,where_part_list):
    print(123)
    """
    循环便利old_dict
    判断是否满足条件
    如果满足在判断select的条件是否为星号
    如果是直接打印
    否则打印出select 条件值的参数
    :param old_dict:
    :param select_part_list:
    :param where_part_list:
    :return:
    """
    for i,v in old_dict.items():
        if where_part_list[2] < old_dict[i].get(where_part_list[0]):
            if len(select_part_list) == 1 and select_part_list[0] == "*":
                print(i,v)
            else:
                for ii in select_part_list:
                    print(ii,v.get(ii))

def dengyu(old_dict,select_part_list,where_part_list):
    for i,v in old_dict.items():
        if where_part_list[2] == old_dict[i].get(where_part_list[0]):
            if len(select_part_list) == 1 and select_part_list[0] == "*":
                print(i,v)
            else:
                for ii in select_part_list:
                    print(ii,v.get(ii))

def xiaoyu(old_dict,select_part_list,where_part_list):
    for i,v in old_dict.items():
        if where_part_list[2] > old_dict[i].get(where_part_list[0]):
            if len(select_part_list) == 1 and select_part_list[0] == "*":
                print(i,v)
            else:
                for ii in select_part_list:
                    print(ii,v.get(ii))

def like(old_dict,select_part_list,where_part_list):
    for i,v in old_dict.items():
        if re.match(where_part_list[2],old_dict[i].get(where_part_list[0])): # re正则匹配开头是否是传入的值
            # if where_part_list[2] == old_dict[i].get(where_part_list[0]): # 先实现where 条件
            if len(select_part_list) == 1 and select_part_list[0] == "*":
                print(i,v)
            else:
                for ii in select_part_list:
                    print(ii,v.get(ii))