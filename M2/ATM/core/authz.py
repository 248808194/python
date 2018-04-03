#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date:2017-01-09-13:05
# Python 3.5

import os,sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(BASE_DIR)
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core import account
from core import  db_handlers
from conf import settings
from core import  logger
from core.hashsecurity import hashsecurity
from conf.settings import admindb
# from core.main import user_status
from core.randomcode import create_random_code

user_status = {
    "isauthz":False,
    "account_id":None,
    'admin_status':False
}


def check_login(func):
    '''
    登录装饰器，更新user_status 来判断用户状态
    :param func:
    :return:
    '''
    def inner(*args,**kwargs):
        if not user_status["isauthz"]:
            exit('请先登录')
        else:
            func(*args,**kwargs)
    return inner


def check_admin(func):
    '''
    管理员装饰器，根据user_status状态判断管理员是否认证
    :param func:
    :return:
    '''
    def inner(*args,**kwargs):
        if user_status['admin_status']:
            func(*args,**kwargs)
        else:
            print("管理员登录失败")
    return inner

def acc_auth(username,password):
    '''
    传入用户名 密码，通过传入的用户名来判断文件是否存在，
    存在则传入正确的用户数据
     判断用户名后在判断传入的密码是否正确，如果正确则返回用户数据，否则返回False
    :param username:
    :param password:
    :return:
    '''
    acc_date = db_handlers.load_user_file(username)
    if acc_date:
        if hashsecurity(password) == acc_date['password']:
            return  acc_date
        else:
            return  False

def acc_login(user_status):
    '''
    输入用户名密码，先匹配admin ，如果匹配管理员用户则，直接返回isadmin
    如果不是，则调用acc_auth函数，
    返回正确的用户数据，则将user_status 下 isauthz 置为真，
    调用logger函数 将登录日志记录到文件中去
    如果密码三次输入错误，直接打印登录３次失败，程序退出 程序退出
    :param user_status:
    :return:
    '''
    retrt_flage = 0
    while user_status['isauthz'] is not True and retrt_flage < 3:
        rancode = create_random_code()
        print('welcome to atm')
        username = input("用户名:")
        password = input("密码:")
        print('\033[32;1m1 验证码:%s \033[0m'%rancode)
        racode = input("验证码:")
        if racode == rancode:
            if username == admindb['adminname'] and hashsecurity(password) == admindb['adminpassword']:
                user_status['admin_status'] = True
                return 'isadmin'
            else:
                acc_date  = acc_auth(username,password)
                # print(acc_date)
                if acc_date:
                    user_status['isauthz'] = True
                    settings.DATABASE['name'] = username
                    logger.logger('denglu','%s login success'%username)
                    return acc_date
                else:
                    print("username or password is worng pls try again")
                    retrt_flage += 1 #拼写错误，retrt---> retry
        else:
            print("验证码不匹配，从新输入")
    else:
        print("登录３次失败，程序退出")
        exit()


