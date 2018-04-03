#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date:2017-01-17-13:29
# Python 3.5

# {2017:[1,2,3,4,5,6]} # dict 年，月
import os,sys,time
# import os,sys
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from conf import settings

# acc_date = {'id': '1234', 'phone': 18964381759, 'limit': 15000, 'balance': 4250.0, 'password': '1234', 'repay': 1000, 'name': 'zhoutao', 'acc_status': 0, 'service_charge': 0.05}
def historys(acc_date):
    '''
    历史账单函数，
    传入用户数据，先拼接出用户日志目录的绝对路径，
    将日志目录下具体的年月放入到user_hist_dict 字典中{'2018': ['01'], '2017': ['01', '02']}
    :param acc_date:
    :return: user_hist_dict
    '''
    current_user_log_dir = settings.BASE_DIR+'/logs/'+acc_date['name']
    year_list = os.listdir(current_user_log_dir)
    print(year_list)
    user_hist_dict  = {}
    for i in year_list:
        user_hist_dict[i] =  os.listdir(current_user_log_dir + '/' + i)
    return user_hist_dict

def print_history(fileabsname):
    '''
    打印账单函数，
    根据用户输入 获得具体日志文件的绝对路径，打印出具体日志内容
    :param fileabsname:
    :return:
    '''
    with open(fileabsname,'r') as  f:
        for i in f:
            i = i.strip()
            print(i)



