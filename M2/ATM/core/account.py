#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date:2017-01-09-10:28
# Python 3.5

# account 账户　余额操作　增加,减少,
import os,sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from conf import  settings
from core import logger


# 将用户账户下的金额进行修改,在写入到文件下去
#
# print(settings.caozuo_leixing)
# 传入 acc_date , 操作类型, money
def account_money_set(acc_date,types,money):
    '''
    账户操作函数，
    传入用户数据，操作类型关键字，具体金额
    还款，转账统一为加钱操作
    如果传入的操作类型合法，先判断是加钱还是减钱操作
    如果是加钱，则将用户数据下的balance余额更新后，
    调用logger函数 将日志记录下来
    返回最新的用户数据
    如果是减钱操作，
    先将具体金额 + 手续费 看原始账户余额是否够减，如果够，则更新 用户账户数据 ，将日志记录下来，返回最新的用户账户信息
    如果不够则直接return false
    :param acc_date:
    :param types:
    :param money:
    :return:
    '''
    # all_money = 0
    if types in settings.caozuo_leixing.keys(): # 加钱操作
        if types == 'huankuan':
            acc_date['balance'] += money
            # print(acc_date)
            all_money = money
            # print('loggertest')
            logger.logger('jiaoyi','用户:%s\t 账户操作\t 动作:%s\t 发生金额:%s\t;余额:%s' % (acc_date['name'], types, all_money, acc_date['balance']))
            return acc_date


        else:
            # print(123,money)
            shouxufei_money = float(settings.caozuo_leixing[types]['shouxufei'] * money) # 减钱操作
            # print('shouxufei_money',shouxufei_money)
            all_money = money + shouxufei_money
            if all_money > acc_date['balance']:
                return False
            else:
                # print(all_money)
                acc_date['balance'] -= all_money
                # print(acc_date)
                logger.logger('jiaoyi', '用户:%s\t 账户操作\t 动作:%s\t 发生金额:%s\t;余额:%s' % (acc_date['name'], types, all_money, acc_date['balance']))
                return acc_date







