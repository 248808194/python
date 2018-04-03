#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date:2017-02-28-14:40
# Python 3.5



#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date:2017-02-28-14:40
# Python 3.5

import json,sys,os,socket,time

class socket_client(object):

    def __init__(self,name):
        '''构造方法传入传入用户名'''
        self.name = name


    def desc(self):
        '''socket客户端连接服务器函数'''
        self.IP_PORT = ('127.0.0.1',9999,)
        self.s = socket.socket()
        self.s.connect(self.IP_PORT)

    def upload(self,upload):
        '''
        连接ｆｔｐ服务端
        发送字典，接受服务端允许发送信息　
        循环发送文件
        关闭连接
        :param upload:
        :return:
        '''
        self.desc()
        send_list = upload.strip().split()
        send_msg = {
            'filename':send_list[1],
            'action':send_list[0],
            'username':self.name,
            'filesize':os.stat('ftp_client/data/%s/%s'%(self.name,send_list[1])).st_size
        }
        # print(send_msg)
        self.s.sendall(bytes(json.dumps(send_msg),encoding='utf8'))
        recv_date = self.s.recv(1024)
        # print(recv_date)
        recv_date = str(recv_date,encoding='utf8')
        if recv_date == '200':
            # print(recv_date)
            filename = send_msg['filename']
            username = send_msg['username']
            with open('ftp_client/data/%s/%s'%(username,filename),'rb') as f:
                for i in f:
                    self.s.sendall(i)
        self.s.close()


    def download(self,download):
        '''
        连接ｆｔｐ服务端
        发送字典，接受服务端允许发送信息　
        服务端开始发送数据
        打开文件，循环写入文件
        关闭连接
        :param upload:
        :return:
        '''
        self.desc()
        download_list = download.strip().split()
        send_msg  = {
            'filename':download_list[1],
            'action':'download',
            'username':self.name,
            'filesize':None
        }
        self.s.sendall(bytes(json.dumps(send_msg),encoding='utf8'))
        date =  self.s.recv(1024).decode()
        if date == '404':
            print('file not found')
        else:
            dict_date = eval(date)
            # print(date,type(date))
            self.s.sendall(b'R')
            with open('ftp_client/data/%s/%s'%(self.name,send_msg['filename']),'wb') as f:
                filesize = 0
                while filesize < dict_date['filesize']:
                    recv_date = self.s.recv(1024)
                    filesize += len(recv_date)
                    f.write(recv_date)
        self.s.close()

    def show_file_list(self):
        '''
        连接ｆｔｐ服务端
        发送字典，接受服务端允许发送信息　
        接受服务端发送的文件列表
        打印出文件列表
        关闭连接
        :param upload:
        :return:
        '''
        self.desc()
        # print(self.s)
        send_msg = {
            'action':'show_file_list',
            'file_list':[],
            'username':self.name
        }

        self.s.sendall(bytes(json.dumps(send_msg),encoding='utf8'))
        data = self.s.recv(1024)
        # print(data)
        data = data.decode()
        if data == '404':
            print('user path is not found')
        else:
            dict_data = eval(data)
            for i in dict_data['file_list']:
                print(i)
        self.s.close()

