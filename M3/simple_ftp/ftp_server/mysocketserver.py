#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date:2017-02-28-14:40
# Python 3.5

import socketserver,json,os
IP_PORT = ("127.0.0.1",9999)
class MYsocketserver(socketserver.BaseRequestHandler):


    def handle(self):
        '''
        接受客户端传入的字典，先解析字典判断动作类型
        通过动作类型来反射出方法
        :return:
        '''
        recv_msg = self.request.recv(1024)
        print(recv_msg)
        recv_msg = str(recv_msg,encoding='utf8')
        recv_msg_dict = json.loads(recv_msg)
        action = recv_msg_dict.get('action')

        if hasattr(self,'%s'%(action)):
            print('hasattr')
            func = getattr(self,'%s'%action)
            func(recv_msg_dict)

    def upload(self,*args,**kwargs):
        '''
        上传方法，传入一个动态参数－通过客户端传来的字典
        通过解析字典来写入文件到服务端
        :param args:
        :param kwargs:
        :return:
        '''
        username = args[0].get('username')
        filename = args[0].get('filename')
        filesize = args[0].get('filesize')
        self.request.sendall(bytes('200',encoding='utf8'))
        with open('ftp_server/userdata/%s/%s'%(username,filename),'wb') as f:
            file_size = 0
            while file_size < filesize:
                recv_date = self.request.recv(1024)
                file_size += len(recv_date)
                f.write(recv_date)


    def download(self,*args,**kwargs):
        '''
        服务端下载方法，读出文件循环的发送给客户端直到发完
        :param args:
        :param kwargs:
        :return:
        '''
        download_dict = args[0]
        filename = download_dict.get('filename')
        username = download_dict.get('username')
        if os.path.exists('ftp_server/userdata/%s/%s'%(username,filename)):
            download_dict['filesize'] = os.stat('ftp_server/userdata/%s/%s'%(username,filename)).st_size
            self.request.sendall(str(download_dict).encode())
            date = self.request.recv(1024).decode()
            if date == 'R':
                with open('ftp_server/userdata/%s/%s'%(username,filename),'rb') as f:
                    for i in f:
                        self.request.sendall(i)
        else:
            self.request.sendall(b'404')


    def show_file_list(self,arg):
        '''查看文件列表方法'''
        tmp_dict = arg
        print(tmp_dict)
        if os.path.exists('ftp_server/userdata/%s'%(tmp_dict['username'])):
            file_list  = os.listdir('ftp_server/userdata/%s'%tmp_dict['username'])
            tmp_dict['file_list'] = file_list
            self.request.sendall(str(tmp_dict).encode())
        else:
            self.request.sendall(b'404')


#


if __name__ == "__main__":
    server = socketserver.ThreadingTCPServer(IP_PORT,MYsocketserver)
    server.serve_forever()