#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date:2016-12-29-09:59
# Python 3.5
import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core import  authz
from core import account
from core import db_handlers
from conf import  settings
from core import logger
from core import historys
from core import managers
from core.authz import user_status
from core.authz import check_login





def accinfo(acc_date):
    '''
    打印出账户信息
    :param acc_date:
    :return:
    '''
    print(acc_date)


@check_login
def xiaofei(acc_date,shop_cash): #待购物商城接入
    '''
    传入账户信息，消费金额
    执行account 下account_money_set 函数
    如果扣款成功则retun 新的账户信息
    :param acc_date:
    :param shop_cash:
    :return:
    '''
    if account.account_money_set(acc_date,'xiaofei',shop_cash):
        return  acc_date

@check_login
def quxian(acc_date):
    '''
    取现函数
    输入数字金额　ｉｎｔ转换为数字　－－＞其实可以在加一个判断是否inp_quxian输入的为数字
    调用account_money_set 函数进行账户具体操作
    :param acc_date:
    :return:
    '''
    inp_quxian = int(input("请输入取现金额:"))
    account.account_money_set(acc_date,'quxian',inp_quxian)

@check_login
def huankuan(acc_date):
    '''
    还款函数
    输入数字金额　
    调用account_money_set 函数进行账户具体操作
    :param acc_date:
    :return:
    '''
    inp_huankuan = int(input('请输入还款金额').strip())
    account.account_money_set(acc_date,'huankuan',inp_huankuan)

@check_login
def zhuanzhang(acc_date):
    '''
    转账函数，输入转入账户名，卡号．
    判断转入账户是否存在，
    如果账户存在
    输入金额
    调用account.account_money_set　先判断账户余额是否足够
        如果足够则调用account.account_money_set函数将转入金额，更新到转入账户中
        将转入账户信息写入到文件下
    如果账户不存在则打印账户不存在
    :param acc_date:
    :return:
    '''
    print('当前可用余额:%s'%acc_date['balance'])
    input_username = input("请输入转入的账户名:")
    inp_userid = input("请输入%s卡号:"%input_username)
    tran_acc_date = db_handlers.load_user_file(input_username)

    if tran_acc_date:
        if tran_acc_date['id'] == inp_userid:# 判断用户名ＩＤ　是否存在
            inp_zhuanzhang  = int(input("请输入转账金额:").strip())
            print('转入用户%s;\t账户%s;\t转入金额:%s'%(input_username,inp_userid,inp_zhuanzhang))
            if account.account_money_set(acc_date,'zhuanzhang',inp_zhuanzhang):
                tran_date = account.account_money_set(tran_acc_date,'huankuan',inp_zhuanzhang) # 加钱
                db_handlers.write_back_file(input_username,tran_date)
    else:
        print('账户不存在')

    #

@check_login
def zhangdan(acc_date):
    '''
    调用　historys函数，先打印出历史账单
    用户输入年/月
    filename 获得具体账单的文件路径
    如果文件存在则调用print_histroy 函数打印出账单
    如果不存在则打印出账单不存在
    :param acc_date:
    :return:
    '''
    print('-现有账单-'.center(40,'-'))
    history_dict = historys.historys(acc_date)
    # print(history_dict)
    for k,v in history_dict.items():
        for i in v:
            print('年:%s-----> %s月份账单\t'%(k,i))

    print('请选择月份默认本年,Example:2017/05')
    inp = input('>:')
    inp_list = inp.split('/')
    filename = '%s/logs/%s/%s/%s/tran.log'%(settings.BASE_DIR,acc_date['name'],inp_list[0],inp_list[1])
    if os.path.exists(filename):
        historys.print_history(filename)
    else:
        print('您要打印的:%s年-%s月 账单不存在'%(inp_list[0],inp_list[1]))

def logout(acc_date):
    '''
    用户退出函数，用户退出时将最新账户信息写入到文件
    :param acc_date:
    :return:
    '''
    print('BYE BYE')
    db_handlers.write_back_file(acc_date['name'],acc_date)
    exit()


def menu(acc_date): #传入账号信息
    '''
    menu_dic  操作类型字典
    输入操作类型，如果操作类型存在与字典中则执行对应的函数，并且传入账户信息

    :param acc_date:
    :return:
    '''
    menu = u'''

        -------  Bank ---------
        \033[32;1m1.  账户信息
        2.  还款
        3.  取现
        4.  转账
        5.  账单
        6.  退出
        7.　消费
        \033[0m
    '''
    menu_dic = {
        '1': accinfo,
        '2': huankuan,
        '3': quxian,
        '4': zhuanzhang,
        '5': zhangdan,
        '6': logout,
        '7': xiaofei,
    }
    print(menu)
    inp = input("\033[32;1m1 chose service type: \033[0m")
    if inp in menu_dic.keys():
        menu_dic[inp](acc_date)



def run(shop_cash=False):
    '''
    调用acc_login模块 传入账户数据
    判断如果acc_date 为管理员用户则执行managers.manager函数，进行后台管理
    如果用户已经认证成功，并且有消费金额传入则直接扣款
    如果用户认证成功，无消费金额，则判断用户为atm登录
    调用menu函数
    :param shop_cash:
    :return:
    '''
    acc_date = authz.acc_login(user_status)
    if acc_date == 'isadmin':
        managers.manager()
    while True:
        if user_status['isauthz']:
            if shop_cash: # 如果传入了消费金额
                if xiaofei(acc_date,shop_cash): # 如果余额足够则为真，打印扣款成功，如果为假则打印扣款
                    db_handlers.write_back_file(acc_date['name'], acc_date)
                    print('扣款成功')
                    return True
                else:
                    print('扣款失败')
                    return False
            else:
                menu(acc_date)


