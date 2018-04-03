#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date:2016-12-29-09:59
# Python 3.5

import os,time

dirtime = time.strftime("%Y|%m",time.localtime()).split('|')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# print(BASE_DIR)

DATABASE = { # 数据存储放弃，其实没用到，后期再说
    'engine': 'file_storage',  # support mysql,postgresql in the future
    'name': None,
    'path': "%s/db" % BASE_DIR

}



logfile = { # 登录的日志类型字典
    'denglu':'access.log',
    'jiaoyi':'tran.log',
}



caozuo_leixing = { # 账户操作类型
'huankuan':{'dongzuo':'zengjia','shouxufei':0}, #+
'quxian':{'dongzuo':'jianshao','shouxufei':0.05}, #-
'zhuanzhang':{'dongzuo':'jianshao','shouxufei':0.05}, #-
'xiaofei':{'dongzuo':'jianshao','shouxufei':0}, #-
}

admindb = { # 管理员用户名密码等
'adminname':'admin',
'adminpassword':'5cb55ec889c8bef0f75ebc4fae801c8d'
}


default_account = { # 添加账户时 初始化的用户数据字典 None为后面需要修改的信息
    "id": None,
    "limit": 15000,
    "service_charge": 0.05,
    "repay": 1000,
    "password": None,
    "name": None,
    "phone": None,
    "balance": 15000,
    "acc_status": 0
}