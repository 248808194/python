#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date:2017-02-04-10:15
# Python 3.5

import re
def unit_mult_div(unit_string): # 计算最小单元的乘除法
    if "*" in unit_string:
        ret = float(unit_string.split('*')[0]) * float(unit_string.split('*')[1])
    else:
        ret = float(unit_string.split('/')[0]) / float(unit_string.split('/')[1])
    return  ret


def remove_mult_div(s):
    if '*' not in s and '/' not in s:
        return s
    else:
        k = re.search(r'-?[\d\.]+[*/]-?[\d\.]+', s).group()
        s = s.replace(k, '+' + str(unit_mult_div(k))) if len(re.findall(r'-', k)) == 2 else s.replace(k, str(unit_mult_div(k)))
        if len(re.findall(r'-',k)) == 2: # 如果在k中发现数据均是负数
            s = s.replace(k,'+' + str(unit_mult_div(k))) # 如果都是负数，则负负得正 将匹配到的最小单元乘除 替换为+ 计算的单元结果 ---》其实就是得到一个正整数
        else:
            s = s.replace(k,str(unit_mult_div(k)))
        return remove_mult_div(s)


def add_sub_str(s): # 加减法
    str1 =  re.findall('([\d\.]+|-|\+)', s) # ()分组
    if str1[0] == '-': #如果第一个数是负数 则需要将数字和负号 进行拼接得到负数
        str1[0] = str1[0] + str1[1] #
        del str1[1]
    ret_sum = float(str1[0])
    for i in range(1,len(str1),2): # 得到加减符号的位置
        if str1[i] =='+' and str1[i+1] != '-': #如果是加法，并且被加的数字为正数
            ret_sum += float(str1[i+1])
        elif str1[i] == '+' and str1[i+1] == '-':#加法，且被加的数为负数
            ret_sum -= float(str1[i+2])
        elif str1[i] == '-' and str1[i+1] == '-': #减法，被减数 为负数
            ret_sum += float(str1[i+2])
        elif str1[i] == '-' and str1[i+1] != '-':
            ret_sum -= float(str1[i+1])
    return ret_sum

def all_prer(s): #四则运算
    s = s.replace(' ', '')
    return add_sub_str(remove_mult_div(s)) # 先计算乘除法，在执行加减法


def cal(s):
    if not re.search(r'\([^()]+\)',s): #如果没有括号 #括号里面没有括号
        return all_prer(s)
    k = re.search(r'\([^()]+\)',s).group()
    s = s.replace(k,str(all_prer(k[1:len(k) - 1])))
    return cal(s)


s = '1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
a = cal(s)
print(a)