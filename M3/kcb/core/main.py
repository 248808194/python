#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date:2017-02-14-13:50
# Python 3.5


from views.manager_view import manager_view
from views.stu_view import stu_view
from views.techer_view import tech_view

# from core.schools import School

def run():
    while True:
        print('''
        请选择管理视图
        １：学生视图
        ２：教师视图
        ３：管理视图
        ''')
        inp1 = input(':>')
        if inp1 == '1':
            stu_view()
        elif inp1 == '2':
            tech_view()
        elif inp1 == '3':
            manager_view()

        else:
            print('输入有误')
