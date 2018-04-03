#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date:2017-01-09-13:04
# Python 3.5

import os,sys


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from conf import settings
from core import db_handlers
from core import authz
from core.authz import user_status
from core.authz import check_admin
from core.hashsecurity import hashsecurity


# @check_admin
def create_user():
    '''
    先load 出初始用户数据 load_new_user_dict
    循环遍历 load_new_user_dict
    来添加用户具体信息
    添加完成将用户数据写入到文件
    :return:
    '''
    load_new_user_dict = settings.default_account
    print('默认添加用户额度15000,')
    for k,v in load_new_user_dict.items():
        if v == None:
            inpv = input('请更改%s:'%k)
            load_new_user_dict[k] = inpv
    print('新用户信息如下')
    for k,v in load_new_user_dict.items():
        print('%s：\t%s'%(k,v))
    load_new_user_dict['password'] = hashsecurity(load_new_user_dict['password']) # 调用自定义加密函数来加密密码
    db_handlers.write_back_file(load_new_user_dict['name'],load_new_user_dict)



# @check_admin
def manager():
    '''
    管理端主程序
    用户选择性操作
    1： 添加用户直接调用create_user函数
    2： 调整额度，修改，
    3: 冻结用户，获得用户数据后直接修改用户数据下的acc_status 值 0为正常，1 为锁定
    :return:
    '''
    while True:
        print('''
        1:添加用户------>    create json file
        2:调整额度------>    change json file
        3:冻结/解冻用户----> change json file
        ''')
        #
        # admin_menu_dcit = {
        #     '1':'createuser',
        #     '2':'change_limits',
        #     '3':'lock/unlock user'
        # }

        admin_select = input('请选择管理员功能:')

        # if admin_select in admin_menu_dcit.keys():
        if admin_select == '1':
            load_new_user_dict = settings.default_account
            create_user()
        elif admin_select == '2':
            print('用户如下')
            print(db_handlers.load_all_userfile())
            chage_username = input('输入要操作的账户姓名:')
            print('用户%s: 目前额度为%s'%(chage_username,db_handlers.load_user_file(chage_username)['limit']))
            acc_date = db_handlers.load_user_file(chage_username) # 通过chage_username获得用户数据
            if acc_date:
                acc_date['limit'] = int(input("请调整用户%s 额度"%acc_date['name'])) # 更新额度value
                db_handlers.write_back_file(chage_username,acc_date)  #写入到文件
            else:
                print('用户不存在')
        elif admin_select == '3':
            print('当前用户如下')
            print(db_handlers.load_all_userfile())
            chage_username = input('输入要操作的账户姓名:')
            acc_date = db_handlers.load_user_file(chage_username)
            if acc_date:
                acc_date['acc_status'] = int(input('冻结/解冻 用户:%s Example 0:unlock\t 1:locked'%(acc_date['name'])))
                db_handlers.write_back_file(chage_username,acc_date)
            else:
                print('用户不存在')

            # admin_menu_dcit[admin_select](acc_date)

        else:
            print("输入错误，请从新输入")


# add_account()