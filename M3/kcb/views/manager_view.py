#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date:2017-02-17-13:47
# Python 3.5

from kcb.core.write_read_obj import Write_Read_Obj as wrb
from kcb.conf import settings

def manager_view(): #管理视图
    school_obj_tuple  = wrb.chose_school() #调用通过pickle的对象序列化文件
    # print(school_obj_tuple)
    school_obj = school_obj_tuple[0]
    obj_pickle_file = settings.school[school_obj_tuple[1]]
    # print(school_obj,obj_pickle_file)

    while True:
        print(
            '''
        请选择管理功能
        １：创建讲师
        ２：创建班级
        ３：创建课程
        4:推出
    　　　　　''')

        inp_chose = input('请选择管理功能：')
        if inp_chose == '1':
            school_obj.create_techer()
        elif inp_chose == '2':
            school_obj.create_class()
        elif inp_chose == '3':
            school_obj.create_lesson()
        elif inp_chose == '4':
            break
        else:
            print('not found try agein')
        #通过pickle更新数据到文件中去
        wrb.write_obj(school_obj,obj_pickle_file)

