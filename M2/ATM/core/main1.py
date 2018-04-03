# #!/usr/bin/env python
# # -*- coding:utf-8 -*-
# # Author: Zhoutao
# #create_date:2016-12-29-09:59
# # Python 3.5
# import os,sys
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# from core import  authz
# from core import account
# from core import db_handlers
# from conf import  settings
# from core import logger
# from core import historys
# from core import managers
# from core.authz import user_status
# from core.authz import check_login
#
# def accinfo(acc_date):
#     print(acc_date)
#
#
# @check_login
# def xiaofei(acc_date,shop_cash): #待购物商城接入
#     # print('beforce acc_date',acc_date)
#     if account.account_money_set(acc_date,'xiaofei',shop_cash):
#         return  acc_date
#
# @check_login
# def quxian(acc_date):
#     inp_quxian = int(input("请输入取现金额:"))
#     account.account_money_set(acc_date,'quxian',inp_quxian)
# @check_login
# def huankuan(acc_date):
#     inp_huankuan = int(input('请输入还款金额').strip())
#     account.account_money_set(acc_date,'huankuan',inp_huankuan)
# @check_login
# def zhuanzhang(acc_date):
#     # 先扣　在加
#     print('当前可用余额:%s'%acc_date['balance'])
#     input_username = input("请输入转入的账户名:")
#     inp_userid = input("请输入%s卡号:"%input_username)
#     tran_acc_date = db_handlers.load_user_file(input_username)
#
#     if tran_acc_date:
#         if tran_acc_date['id'] == inp_userid:# 判断用户名ＩＤ　是否存在
#             inp_zhuanzhang  = int(input("请输入转账金额:").strip())
#             print('转入用户%s;\t账户%s;\t转入金额:%s'%(input_username,inp_userid,inp_zhuanzhang))
#             if account.account_money_set(acc_date,'zhuanzhang',inp_zhuanzhang):
#                 tran_date = account.account_money_set(tran_acc_date,'huankuan',inp_zhuanzhang) # 加钱
#                 db_handlers.write_back_file(input_username,tran_date)
#     else:
#         print('账户不存在')
#
#     #
#
# # acc_date = {'id': '1234', 'phone': 18964381759, 'limit': 15000, 'balance': 4250.0, 'password': '1234', 'repay': 1000, 'name': 'zhoutao', 'acc_status': 0, 'service_charge': 0.05}
# @check_login
# def zhangdan(acc_date):
#     print('-现有账单-'.center(40,'-'))
#     history_dict = historys.historys(acc_date)
#     # print(history_dict)
#     for k,v in history_dict.items():
#         for i in v:
#             print('年:%s-----> %s月份账单\t'%(k,i))
#
#     print('请选择月份默认本年,Example:2017/05')
#     inp = input('>:')
#     inp_list = inp.split('/')
#     filename = '%s/logs/%s/%s/%s/tran.log'%(settings.BASE_DIR,acc_date['name'],inp_list[0],inp_list[1])
#     if os.path.exists(filename):
#         historys.print_history(filename)
#     else:
#         print('您要打印的:%s年-%s月 账单不存在'%(inp_list[0],inp_list[1]))
#
#
#     # 先执行historys　函数
#     # 打印出来所有的日志文件
#     # 在拼接出文件
#     # 将拼接出的文件传入给print_history来执行
#
#
# def logout(acc_date):
#     print('BYE BYE')
#     db_handlers.write_back_file(acc_date['name'],acc_date)
#     exit()
#
#
# def menu(acc_date): #传入账号信息
#     menu = u'''
#
#         -------  Bank ---------
#         \033[32;1m1.  账户信息
#         2.  还款
#         3.  取现
#         4.  转账
#         5.  账单
#         6.  退出
#         7.　消费
#         \033[0m
#     '''
#     menu_dic = {
#         '1': accinfo,
#         '2': huankuan,
#         '3': quxian,
#         '4': zhuanzhang,
#         '5': zhangdan,
#         '6': logout,
#         '7': xiaofei,
#     }
#     print(menu)
#     inp = input("\033[32;1m1 chose service type: \033[0m")
#     if inp in menu_dic.keys():
#         menu_dic[inp](acc_date)
#
#
#
# def run(shop_cash=False):
#     acc_date = authz.acc_login(user_status)
#     while True:
#         if user_status['isauthz']:
#             if shop_cash: # 如果传入了消费金额
#                 if xiaofei(acc_date,shop_cash):
#                     db_handlers.write_back_file(acc_date['name'], acc_date)
#                     print('扣款成功')
#                     return True
#                 else:
#                     print('扣款失败')
#                     return False
#             else:
#                 menu(acc_date)
#
#
