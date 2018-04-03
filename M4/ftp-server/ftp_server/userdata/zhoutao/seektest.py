#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date:2017-04-11-09:30
# Python 3.5
import os
count = 0
with open('100.img','rb') as f:
    with open('100.new.new','wb') as fnew:
        while True:
            data = f.read(1024*1024)  # 1m
            if not data:
                break
            count +=len(data)
            print(count)
            fnew.write(data)
            if count > 19922944:
                break

import time
time.sleep(10)

file_size = os.stat('100.new.new').st_size

with open('100.img','rb') as f:
    f.seek(file_size)
    with open('100.new.new','ab+') as ff:
        while True:
            data = f.read(1024*1024)
            if not data:
                break
            ff.write(data)
