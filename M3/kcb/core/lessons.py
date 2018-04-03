#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date:2017-02-14-13:49
# Python 3.5


class Lesson(object):
    '''课程类'''
    def __init__(self,lesson_name,lesson_price,lesson_perid):
        self.lesson_name = lesson_name
        self.lesson_price = lesson_price
        self.lesson_perid = lesson_perid
        print(self.lesson_name,self.lesson_perid,self.lesson_price)
