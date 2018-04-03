#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date:2017-02-27-11:23
# Python 3.5
from conf import settings
import pickle

class Write_Read_Obj(object):
    '''序列化反序列化类'''


    @staticmethod
    def chose_school():
        '''选择学校'''
        for i in settings.school.keys():
            print('当前校区 %s' % i)
        chose_inp = input('请选择校区进行操作：')
        if chose_inp not in settings.school.keys():
            print('您选择的校区不存在')
        else:
            redobj = Write_Read_Obj.read_obj(chose_inp)
            return redobj

    @staticmethod
    def write_obj(obj,file):
        '''静态方法，写文件序列化对象'''
        with open(file, 'wb') as f:
            pickle.dump(obj,f)


    @staticmethod
    def read_obj(file):
        '''静态方法，反，　读取对象文件'''
        with open(settings.school[file], 'rb') as f:
            shcool_obj = pickle.load(f)
            return shcool_obj,file