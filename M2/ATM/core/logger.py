#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date:2017-01-12-16:59
# Python 3.5

#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date:2017-01-09-10:28
# Python 3.5

import logging

import  logging,time,sys,os,time
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from conf import settings

def logger(logtype,message):
    '''
    日志接口函数
    日志文件的保持方式为/username/years/mouth/...log
    通过传入的日志类型 ，得到具体的日志文件路径./名称等
    :param logtype:
    :param message:
    :return:
    '''

    #global setting
    logger = logging.getLogger(logtype)
    logger.setLevel(logging.DEBUG)

    # to mirror
    input_mirror = logging.StreamHandler()
    input_mirror.setLevel(logging.DEBUG)

    # to file
    dirtime = time.strftime("%Y|%m", time.localtime()).split('|') # 获得当前年，月列表
    user_log_path  = "%s/logs/%s/%s/%s"%(settings.BASE_DIR,settings.DATABASE['name'],dirtime[0],dirtime[1]) # 获得目录变量
    os.makedirs(user_log_path,exist_ok=True) # 先创建log目录
    log_file = "%s/%s"%(user_log_path,settings.logfile[logtype])
    # print(log_file,123)
    input_file = logging.FileHandler(log_file)
    input_file.setLevel(logging.DEBUG)

    # fomart input type
    format_type = logging.Formatter("%(asctime)s  - %(message)s")

    # user format type
    input_mirror.setFormatter(format_type)
    input_file.setFormatter(format_type)


    logger.addHandler(input_mirror)
    logger.addHandler(input_file)
    logger.debug(message)
    logger.removeHandler(input_file)
    logger.removeHandler(input_mirror)
    # return logger
