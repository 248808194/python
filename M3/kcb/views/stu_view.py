#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date:2017-02-17-13:34
# Python 3.5

import pickle
from conf import settings
from kcb.core.students import Students
from kcb.core.write_read_obj import Write_Read_Obj as wrb
from kcb.core.schools import School




def stu_view(): #学生视图
    # School = School
    for i in settings.school.keys():
        print('当前校区如下%s'%i)
    inp_sch = input('请选择校区:')
    if inp_sch in settings.school.keys():
        school_path = settings.school[inp_sch]
        print(school_path)
        shcool_obj = wrb.read_obj(inp_sch)[0]
        print(shcool_obj.SCHOOL_CLASS)
        stu_inp_name = input('请输入新学员姓名:')
        stu_obj = Students(stu_inp_name,shcool_obj)
        stu_inp_money = int(input('请输入学费:'))
        stu_obj.register(stu_inp_money)
        print(shcool_obj.SCHOOL_STUDENTS)
        inp_chose = input("是否需要现在选择班级Y/N")
        if inp_chose == 'Y' or inp_chose == 'y':
            stu_obj.chose_class()
            print(shcool_obj.SCHOOL_CLASS)
            wrb.write_obj(shcool_obj,school_path)

        else:
            pass

    else:
        print("输入错误，您选择的校区不存在")

#     # 学员直接选择校区缴费后注册到某戈班级开始学习
# with open('/home/zt/PycharmProjects/51cto_python_homework/M3/课程表/db/sh_school','rb') as f:
#     shcool_obj = pickle.load(f)
#     print(shcool_obj.SCHOOL_TECHER )
#     print(shcool_obj.SCHOOL_CLASS )
#     print(shcool_obj.SCHOOL_LESSON )



