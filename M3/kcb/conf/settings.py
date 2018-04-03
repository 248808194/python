#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date:2017-02-16-17:35
# Python 3.5

import sys,os,time,datetime,json,pickle
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


school = {
    'sh_school': os.path.join(BASE_DIR,'db','sh_school'),
    'bj_school': os.path.join(BASE_DIR,'db','sh_school')
}


print(school)
