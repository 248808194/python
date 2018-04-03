#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date:2016-10-24-11-07
# Python 3.5



import re
import menu



def login(u_name,u_passwd): # 用户登录
    user_tmp_list = {} #数据格式 #{"username",["password","flag"]}
    with open("userdb", "r") as db: #读取userdb文件， 将用户名 密码，标志位放到user_tmp_list字典中
        for line in db:
            line = line.strip().split("|")
            tmp_list = []
            tmp_list.extend([line[1], line[2]])  # extend 一个列表包含密码,flag标志位
            user_tmp_list[line[0]] = tmp_list

    user_tmp_list.get(u_name,"notfound") # 获取用户flag 位
    user_tmp_list.keys() # 获取所有的键
    if u_name in  user_tmp_list.keys():
        if user_tmp_list.get(u_name)[1] == "1": # 先检查用户是否锁定
            print("用户锁定，程序退出")
            exit()
        else:
            if u_passwd == user_tmp_list.get(u_name)[0]: # 未锁定检查密码是否匹配
                return True #返回 True 表示用户通过验证
            else:
                return  "notmatch" # 返回 motmatch表示 密码不对

    else:
        return  False # 返回False 表示用户名未找到

def lock_user (u_name): # 用户锁定函数
    with open("userdb", "r") as db:
        lines = db.readlines() # 先把文件读取到内存
        with open("userdb", "w") as db:
            for i in lines:
                if i.startswith(u_name):
                    db.write(re.sub("0", "1",i)) #逐行匹配，读一行，写一行
                else:
                    db.write(i)

def main(): #主函数
    a = 0 # 锁定判断标志位
    while True:
        if a == 3:# 用户输入超过3次执行lock函数并退出循环
            lock_user(u_name)
            print("尝试3次登录失败，用户%s 锁定 程序退出"%(u_name))
            break
        else:
            u_name = input("Enter your username:")
            u_passwd = input("Enter you password:")
            if login(u_name,u_passwd)  == "notmatch":#如果login函数返回的结果为False则让a自加1
                a+=1
                continue
            elif login(u_name,u_passwd) == False:
                print("user %s not exists" %u_name)
                continue
            else:
                menu.menu()


if __name__ == "__main__":
    main()

