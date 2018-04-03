#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date:2016-10-25-14-41
# Python 3.5

"""
1. 商品信息- 数量、单价、名称
2. 用户信息- 帐号、密码、余额
3. 用户可充值
4. 购物历史信息
5. 允许用户多次购买，每次可购买多件
6. 余额不足时进行提醒
7. 用户退出时 ，输出档次购物信息
8. 用户下次登陆时可查看购物历史
9. 商品列表分级显示


用户登录模块
注册模块
购买模块
充值模块
购物车模块
"""
import re
import json
import time
import os,sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
from core import main as atmain


json_dict=json.load(open("prodlist.json","r")) #read json file to json_dict -(dict)
# print(json_dict)
# json_dict.get("手机").get("sonyp1")[1] =39 #(change some value )
json.dump(json_dict,open("prodlist.json","w")) #(change value write to json (will change data value ))


def read_json():
    json_dict = json.load(open("prodlist.json", "r"))
    return json_dict


def write_json(price_name,leixing,shuliang):
    a=read_json()
    c = str (int(a.get(price_name).get(leixing)[1]) - int(shuliang)) #更新库存数量
    a.get(price_name).get(leixing)[1] = c
    json.dump(a, open("prodlist.json", "w")) #更新json文件


#购买函数
#u_name,price_name,price_name2,shuliang

def chongzhi (u_name):
    with open("userdb","r") as db:
        for i in db:
            i = i.strip().split("|")
            if u_name == i[0]:
                # print("%s current money is %s"%(u_name,i[3] ))
                old_money = i[3] #临时存放余额
                while True:
                    inp_money=input("pls recharge your account:")
                    if str.isdigit(inp_money) == True:
                        a = []  # 定义一个空列表用于存放userdb修改后的数据
                        with open("userdb", "r") as db:  # 将userdb 逐行读取到lines列表中
                            for i in db:
                                i = i.strip().split("|")
                                if i[0] == u_name:  # 如果用户名存在则修改用户当前的余额
                                    i[3] = str(int(inp_money) + int(old_money)) #先转换为int做加法运算在转换为str 修改列表值
                                    print("recharge account success ,current money is %s" % i[3]) #打印充值后的余额
                                    a.append(i)
                                else:
                                    a.append(i)
                        with open("userdb", "w") as db:
                            for i in range(len(a)):
                                b = "|".join(a[i]) + "\n"  # 将a列表中的子列表转换成字符串，写入到db中去
                                db.write(b)
                        return "success"
                    else:
                        print("worng input pls input number not character")
                        continue



def koukuan (u_name,zongjia):
    atmain.run(zongjia)
    # main.run(shop_cash = zongjia)
    # 扣款直接调用atm主函数,传入需要扣款的金额如果返回为真　则说明扣款成功

def buy(u_name):
    with open("userdb", "r") as db:# 临时存放余额
        old_money = ""
        for i in db:
            i = i.strip().split("|")
            if u_name == i[0]:
                print("%s current money is %s" % (u_name, i[3]))
                old_money = i[3]
                price_name = input("输入购买类型") #购买项目手机，洗衣机
                leixing = input("输入型号:") #购买型号
                shuliang = input("输入购买数量:") #购买数量
                danjia = int(json_dict.get(price_name).get(leixing)[0])  # 获取商品单价
                zongjia = danjia * int(shuliang)  # 商品总价
                if int(zongjia) < int(old_money):  # 总价小于余额
                    with open(u_name + "_cart_histtory", "a") as history:
                        history.write(time.ctime() + "|" + leixing + "|" + shuliang + "|" + str(zongjia) + "\n")
                    if koukuan(u_name, zongjia) == True:
                        write_json(price_name, leixing, shuliang) #更新库存
                        continue_buy = input("是否继续购物Y/N:")
                        if continue_buy == "Y":
                            continue
                        elif continue_buy == "N":
                            user_his(u_name)
                            exit()
                else:
                    print("current money is not enough")
                    chongzhi(u_name)

    print(json_dict.get(leixing))

    tmp_list = []
    for i in json_dict.values():
        for i in i.keys():
            tmp_list.append(i)


#商品列表函数
def show_list():#商城库存函数
    print("当前售卖商品:")
    for i in json_dict.keys():  # 获取json_dict的所有键
        print(i, ":")
        a = (json_dict.get(i))
        for key, value in a.items():  # 获取json_dict 值（子字典）得所有键，和值
            print("\t\t%s:\t 价格:%s\t 库存:%s\t" % (key, value[0], value[1]))

#登陆函数
def login (u_name,u_passwd):#登陆函数
    with open("userdb","r") as db: #讲用户名保存到临时列表中
        tmp_user_list = []
        for i in db:
            i  = i.strip().split("|")
            tmp_user_list.append(i[0])
        if u_name not  in tmp_user_list:#如果用户名不存在，程序退出，return 注册关键字
            return "register"
    with open ("userdb","r") as db:
        for i in db:
            i = i.strip().split("|")
            if i[2] == "1":
                return "lock"
            if u_name  ==  i[0] and u_passwd == i[1]: #用户名密码正确
                return True
            elif u_name ==i[0] and u_passwd != i[1]:#用户名正确，密码错误
                return  False
            else:
                continue

#注册函数
def register (u_name,u_passwd):#注册函数
    with open("userdb","a") as db:
        i = "\n" + u_name + "|"+ u_passwd + "|" + "0" + "|" + "0"
        db.write(i)

#锁定用户函数
def lock_user(u_name): #锁定函数
    a=[] #定义一个空列表用于存放userdb修改后的数据
    with open("userdb", "r") as db: #将userdb 逐行读取到lines列表中
        for i in db:
            i=i.strip().split("|")
            if i[0] == u_name:#如果用户名存在则将锁定标示符置为1
                i[2] = "1"
                a.append(i)
            else:
                a.append(i)
    with open("userdb","w") as db:
        for i in range(len(a)):
            b="|".join(a[i])+"\n" #将a列表中的子列表转换成字符串，写入到db中去
            db.write(b)

#充值函数

#历史订单好书
def user_his(u_name):
    try:
        print("当前用户购物历史信息")
        with open(u_name + "_cart_histtory", "r") as history:
            for i in history:
                i = i.strip().split("|")
                print("购买时间:{0}\t\t 物品名称:{1}\t\t  数量:{2}\t\t  总价:{3}".format(i[0], i[1], i[2], i[3]))

    except Exception as ex:
        print("当前用户没有历史订单")


#主函数
def main (): #主函数
    lock_flag = 0
    while True:
        if lock_flag == 3:
            print("password input worng 3th lock user")
            lock_user(u_name)
            break
        u_name = input("enter your username:")
        u_password = input("enter you password:")
        if login(u_name,u_password) == "register": #如果返回register 执行注册程序，注册用户
            print("%s is new user will be register "%u_name)
            register(u_name,u_password)
            continue
        elif login(u_name,u_password) == "lock":#如果返回时lock 跳出重新输入
            print("user is locked ")
            continue
        elif login(u_name,u_password) == False:
            print("password is not match pleas try again")
            lock_flag += 1
            continue
        elif login(u_name,u_password) == True:
            while True:
                print("""
                登陆成功
                请选择操作
                A：查看历史购物信息
                C: 购物:\n
                """)
                chose = input(">>>:")
                if chose == "A": #history
                    user_his(u_name)
                    continue
                # elif chose == "B": #rechage
                #     chongzhi(u_name)
                elif chose == "C": #shop
                    show_list() #打印商城库存列表
                    buy(u_name)

                else:
                    print("you got an worng input pls input string of  A/B/C")
                    continue #z#主韩主函数



if __name__ == "__main__":
    main()

