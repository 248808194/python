#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date:2017-04-12-09:31
# Python 3.5

from db.db_dict import server_dict
import threading
from core.SSH import SSH


def main():
    def create_threading(chose_host_list):
        '''
        循环获取每个主机的用户名，端口，密码等，
        :params server_list: 获取到连接参数后以列表元祖的格式放如server_list 中，并return 出去
        :return:
        '''
        server_list = []
        for i in chose_host_list:
            host = i
            port = server_dict[i]['port']
            username = server_dict[i]['username']
            password = server_dict[i]['password']
            tuple_arg = (host, port, username, password,)
            server_list.append(tuple_arg)
        return server_list

    while True:
        chose_host_list = []
        host_list = [ x for x in server_dict.keys()]
        # print(host_list)
        print('列表如下:'.center(40,'='))
        for i in host_list:print(i+'\t')
        chose_host = input("选择操作的主机或者主机组:")
        # print('主机列表如下\n',host_list)
        if chose_host == '*': # 选择所有主机
            chose_host_list = host_list
        elif len(chose_host) == 0:continue
        else:
            chose_host_list  = (chose_host.strip().split())
            for each_inp_host in  chose_host_list:
                if each_inp_host in host_list:
                    pass
                else:
                    print('主机:%s不在数据库中剔除'%(each_inp_host))
                    chose_host_list.remove(each_inp_host)
                    if len(chose_host_list) ==0:continue #主机均不在数据库中
        print('此次操作的主机如下',chose_host_list) #存放的主机列表
        while True: #循环的操作主机命令
            t_list = [] #多线程空列表
            action_dict = {1:'command',2:'upload',3:'download'}
            help_msg = '''
            请选择
            1：执行参数
            2：上传文件
            3：下载文件:
            '''
            input_action = input(help_msg+'\n:')
            if input_action in action_dict.keys():
                pass
            elif input_action == 'exit':break
            elif input_action == '1':
                inp_command = input('请输入命令:')
                for i in create_threading(chose_host_list):
                    t_list.append(threading.Thread(target=SSH(i).comm,args=(inp_command,)))

            elif input_action == '2':
                files = input("输入本地文件 服务器文件Example：localfile remotefile:").strip().split()
                for i in create_threading(chose_host_list):
                    t_list.append(threading.Thread(target=SSH(i).upload,args=(files[0],files[1],)))

            elif input_action == '3':
                files = input("输入本地文件 服务器文件Example： remotefile localpath:").strip().split()
                for i in create_threading(chose_host_list):
                    t_list.append(threading.Thread(target=SSH(i).download, args=(files[0], files[1],)))

            else:
                print('命令不存在，从新输入')
                continue
            for i in t_list:
                i.start()
            for i in t_list:
                i.join()
            print('执行完毕')













if __name__ == '__main__':
    main()
