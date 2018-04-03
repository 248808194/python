#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date:2017-01-09-10:30
# Python 3.5
import os,sys,json
#
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
#
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
from conf import settings

def load_user_file(username):
    '''
    获取用户数据函数
    根据传入的用户名来拼接用户数据文件绝对路径
    如果文件存在，则判断用户名正确，通过json序列化出acc_date字典 return 用户字典
    否则 return false
    :param username:
    :return: acc_date
    '''
    user_json_file = '%s/db/accounts/%s.json' %(BASE_DIR,username)

    if os.path.isfile(user_json_file):
        acc_date = json.load(open(user_json_file,'r'))
        return acc_date
    else:

        return False


def write_back_file(username,acc_date):
    '''
    更新用户数据函数
    通过用户名，最新的用户数据，将最新数据更新到文件
    :param username:
    :param acc_date:
    :return:
    '''
    user_json_file = '%s/db/accounts/%s.json' %(BASE_DIR,username)
    json.dump(acc_date,open(user_json_file,'w'),indent=4)
    return True



def load_all_userfile():
    '''
    为manager管理函数服务，打印出accounts下所有的json文件，并且通过字符串替换过滤到用户名，
    返回出所有的用户名列表
    return [ 'username1','username2'........ ]
    :return:
    '''
    account_dir = '%s/db/accounts'%BASE_DIR
    # print(account_dir)
    alllist = os.listdir(account_dir)
    ilist = []
    for i in alllist:
        i = i.replace('.json','')
        ilist.append(i)

    ilist = [x.replace('.json','') for x in alllist]
    return ilist







