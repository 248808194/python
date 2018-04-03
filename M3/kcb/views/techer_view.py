#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date:2017-02-24-16:40
# Python 3.5


from core.techers import Techer
from kcb.core.write_read_obj import Write_Read_Obj as wrb

def tech_view(): #老师视图
    #讲师先登录
    enter_techer_name  = input('请输入讲师姓名：')
    tech_obj = Techer(enter_techer_name)
    school_obj = tech_obj.check_name_in_school()[0]
    school_path = tech_obj.check_name_in_school()[1]
    while True:
        if school_obj:
            print('''
             1:查看学员花名册
             2：选择授课班级
            ''')
            inp_chose = input('请选择操作')
            if inp_chose == '1':
                tech_obj.check_stu_list(school_obj)
                inp_ch = input('是否修改学生成绩:Y/N') # Y/N
                if inp_ch == 'Y' or inp_ch == 'y':
                    stu_name = input('选择学生:')
                    stu_new_score = input('从新设定分数')
                    tech_obj.change_stu_score(school_obj,stu_name,stu_new_score)
                    wrb.write_obj(school_obj, school_path)
                elif inp_ch == 'N' or inp_ch == 'n':
                    continue

            elif inp_chose == '2':
                tech_obj.chose_class(school_obj)
                break


        else:
            print('教师未找到,从新输入')