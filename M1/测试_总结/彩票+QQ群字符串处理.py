#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date:2016-11-09-14-31
# Python 3.5

#无聊的彩票预测
import  random
base_ball = "31,27,35,16,17,34,03,13,11,15,12,01,30,20,23,07,02,09,14,18|07,08,03,05"
b = [i for i in base_ball.strip().split("|")]
red_ball = []
blue_ball = []
while True:
    if len(red_ball) < 5:
        single_red_ball = random.choice(b[0].strip().split(","))
        if single_red_ball in red_ball:
            continue
        else:
            red_ball.append(single_red_ball)
    else:
        if len(blue_ball) < 2:
            single_blue_ball = random.choice(b[0].strip().split(","))
            blue_ball.append(single_blue_ball)
        else:
            break

print("篮球:",red_ball, "\t\t\t" ,"红球:",blue_ball)


#字符串凭借
#将aa这个字符串每隔5个字符添加|符号
# import re
# aa = "aaaaabbbbbcccccddd"
# tmp_str = ""
# # for i in range(1,len(aa),5):
# for i in range(0,len(aa),5): #range 步进方法 5个一步进
#     # tmp_str +=aa[i-1:i+4] + "|" # 只能5个字符，并且最后一位拼接|
#     tmp_str +=aa[i:i+5] + "|" # 只能5个字符，并且最后一位拼接|
#     # tmp_str += "|".join(list(aa[i:i+5]))
# # tmp_str = tmp_str[:-1] # 将最后的|去掉，得到 aaaaa|bbbbb|ccccc|ddd
# print(tmp_str)

