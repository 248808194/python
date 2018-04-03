#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date:2017-03-06-16:07
# Python 3.5


from ftp_client.socket_class import socket_client
import sys,os


class Login_func(object):
    def __init__(self,name):
        '''
        主逻辑构造函数
        传入名字来实例化客户端类
        :param name:
        '''
        self.list_dict = {
            '1':'download_file',
            '2':'upload_file',
            '3':'check_file_list'
        }
        self.name = name
        self.socket_client = socket_client(self.name)
        # print(self.socket_client)


    def check_user_exists(self):
        '''目录名定义为用户名　，查看目录是否存在就是在查看用户是否存在
        存在返回真，不存在返回假
        '''
        if os.path.exists('ftp_server/userdata/%s'%self.name):
            return True
        else:
            return False


    def download_file(self,enter):
        '''下载文件'''
        self.socket_client.download(enter)


    def upload_file(self,enter):
        '''上传文件'''
        self.socket_client.upload(enter)

    def check_file_list(self):
        '''查看文件列表'''
        self.socket_client.show_file_list()



def main():
    '''
    先登录
    判断用户是否存在
    存在打印出菜单，通过反射调用实例化Login_func后的方法
    不存在打印出用户名不存在

    :return:
    '''
    print('login first')
    name = input("username:")

    logname = Login_func(name)

    if logname.check_user_exists():
        while True:
            for k,v in logname.list_dict.items():
                print(k,':',v)
            enter_chose = input('enter your chose  1/2/3:')
            if enter_chose == '3':
                logname.check_file_list()
            else:
                if hasattr(logname,logname.list_dict[enter_chose]):
                    func = getattr(logname,logname.list_dict[enter_chose])
                    ent = input('EXAMPLE: download test.txt / upload test.txt ')
                    func(ent)


    else:
        print('user not found')

if __name__ == '__main__':
    main()