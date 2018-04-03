#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date:2017-04-11-10:48
# Python 3.5

count = 0
#如果不确认文件大小
with open('100.img','rb') as f:
    with open('100.new.new','wb') as fnew:
        while True:
            data = f.read(1024*1024)  # 1m
            if not data:
                break
            count +=len(data)
            print(count)
            fnew.write(data)
            # if count > 19922944:
            #     fnew.flush()
            #     fnew.close()
            #     break
