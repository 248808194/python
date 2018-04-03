#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date:2017-02-07-10:01
# Python 3.5


a = input(">>>:")
try:
    a.isdigit()
    print(int(a)+1)
except Exception as e:
    print(e)
finally:
    print("programs is finished")