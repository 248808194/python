#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date:2016-11-03-10-34
# Python 3.5

user_tmp_lsit = {}
with open("userdb", "r") as db:
    for line in db:
        line = line.strip().split("|")
        tmp_list = []
        tmp_list.extend([line[1],line[2]]) # extend
        user_tmp_lsit[line[0]] = tmp_list



print(user_tmp_lsit)
