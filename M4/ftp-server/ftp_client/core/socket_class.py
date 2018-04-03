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

import json,sys,os,socket,time,re
from tqdm import  tqdm
import sys,os,hashlib
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# from  core.md5_encrypt import hashsecurity

class socket_client(object):

    def __init__(self):
        '''构造函数'''
        self.user_path = None #用户路径
        self.username = None #用户名
        self.host = '127.0.0.1' #server端ip
        self.port = 9999 #server端口
        self.client = socket.socket() #初始化socket
        self.conn_server() #连接到ftpserver
        self.command_call() #执行call方法

    def conn_server(self):
        '''连接服务器方法'''
        try:
            self.client.connect((self.host,self.port))
        except Exception as e:
            print('server is dissconnect')

    def command_call(self):
        current_path = self.login()
        print('欢迎%s来到ftpserver' % self.username)
        self.ftp_help()
        while True:
            user_info_discplay = ('[%s@%s]%s:'%(self.username,self.host, self.user_path)) #拼凑出一个类似命令行提示符 Example： [zhoutao@127.0.0.1]userdata/zhoutao:
            self.command_input = input(user_info_discplay).strip().split() #用户输入方法文件名，通过split来组成一个2位的列表
            if len(self.command_input) == 0: continue #输入为空则返回继续输入
            command_method = self.command_input[0] #获取到用户方法
            # print(command_method)
            if hasattr(self,command_method): #通过反射去执行具体的方法
                # print('hasattr')
                func = getattr(self,command_method)
                func()
            else:
                print('输入错误请从新输入') #如果不存在则判定输入错误，返回并且打印ftp_help信息
                self.ftp_help()
                continue

    def login(self):
        '''
        客户端登录验证函数
        密码输错三次退出程序
        :return:
        '''
        count = 0
        while True:
            print('请先登录')
            if count > 3:
                print('密码输错3次，程序退出')
                self.client.close()
                exit()
            username = input('username:')
            password = input('password:')
            # username = 'zhoutao'
            self.username = username
            # password =  '123456'

            if not username or  not password:print('username or password can not be set emputy');continue #用户名密码不能为空
            hashmd5 = hashlib.md5()
            hashmd5.update(password.encode())
            password = hashmd5.hexdigest() #加密用户密码
            # self.m.update(password.encode())

            login_dict = {'action':'login','username':username,'password':password} #构成登录字典
            json_str = json.dumps(login_dict)
            self.client.send(json_str.encode()) #json序列化登录字典发送给客户端
            server_check_result  = self.client.recv(4096) #接受服务端传来的验证信息200 true 403 false
            # print('server_check_result',server_check_result)
            if server_check_result == b'403':
                print(server_check_result.decode(),'密码错误请从新输入')
                count +=1
                continue
            else:
                self.user_path = server_check_result.decode()
                return self.user_path #返回用户主目录

    def view_bar(self,num, total):
        '''进度条方法'''
        rate = float(num) / float(total)
        rate_num = int(rate * 100)
        r = '\r%s>%d%%' % ('=' * rate_num, rate_num,)
        sys.stdout.write(r)
        sys.stdout.flush()

    def get(self):
        '''客户端下载方法'''
        mget = hashlib.md5()
        get_dic = {'action':'get','filename':os.path.join(self.user_path,self.command_input[1]),'username':self.username,'client_file_tmp_size':0} #get命令字典
        self.client.send(str(get_dic).encode()) #发送命令字典给服务器端
        file_full_path = os.path.join(BASE_DIR,get_dic.get('filename')) #客户端文件绝对路径
        client_file_tmp_size = get_dic['client_file_tmp_size']
        tmp_size = 0  # 初始化值
        file_total_size = self.client.recv(4096)  # 从服务器端收到的原始文件大小
        # print('file_total_size is ',file_total_size)
        file_total_size = int(file_total_size)
        if os.path.isfile(file_full_path): #如果文件存在，判断大小
            client_file_tmp_size += os.stat(file_full_path).st_size #默认假设文件大小为0，与当前文件做自加操作得到真实的文件大小
            if client_file_tmp_size < file_total_size: #如果小于则判定文件未能传完，需要开始断点续传
                file_total_size -=client_file_tmp_size #得到文件还需要传输多少字节
                print('文件%s未传完，开始断点续传'%(self.command_input[1]))
            elif client_file_tmp_size == file_total_size: #如果是等于则文件已经传输完成，并且客户端已经存在
                # print(client_file_tmp_size,file_total_size)
                print('文件%s 已经存在'%(self.command_input[1]))
                self.client.send(b'1000') #发送1000给客户端，这里有bug，只能用1000来处理
                return True #直接return 退出get方法

        self.client.send(str(client_file_tmp_size).encode()) #发送客户端文件大小，如果文件不存在为0 ，主要配合server端seek值
        with open(file_full_path, 'ab+') as f: #循环接受文件，做MD5对比，
            # print(tmp_size,999)
            while tmp_size < file_total_size:
                if file_total_size - tmp_size > 4096:
                    size = 4096
                else:
                    size = file_total_size - tmp_size
                tmp_file = self.client.recv(size)
                tmp_file_size = len(tmp_file)
                tmp_size += tmp_file_size
                f.write(tmp_file)
                self.view_bar(tmp_size, file_total_size)
                mget.update(tmp_file)
            else:
                file_md5 = mget.hexdigest()
                # print('client file md5 is ', file_md5)
                server_file_md5 = self.client.recv(4096).decode()
            if file_md5 == server_file_md5:
                print('file:%s get  done ' % (self.command_input[-1]))
            else:
                print('file:%s check md5 value can not math' % (self.command_input[-1]))

    def put(self):
        mget = hashlib.md5()
        put_dic = {'action':'put','filename':os.path.join(self.user_path,self.command_input[1]),'username':self.username} #动作字典
        filename = os.path.join(BASE_DIR,put_dic['filename']) #客户端拼接文件绝对路径
        self.client.sendall(str(put_dic).encode()) #将字典发送给服务端
        du_dic_from_server = self.client.recv(4096) #接受服务器段发来的剩余磁盘空间大小
        # print('bits du dic from server')
        du_dic_from_server = eval(du_dic_from_server)
        # print('eval from server du dic is ',du_dic_from_server)
        # print('du dic from server is ',du_dic_from_server)
        if '200' in du_dic_from_server.keys(): #这里修改一个字典{'200': 剩余空间}
            file_size = os.stat(filename).st_size
            if int(du_dic_from_server['200']) > file_size:
                self.client.sendall(str(file_size).encode()) #有足够空间，发送文件大小给服务端
                if self.client.recv(4096) == b'R': #接受到R关键字，客户端开始发送文件
                    len_tmp_data = 0
                    with open(filename,'rb')as f: #循环发送文件
                        # print('in open file')
                        for i in f:
                            len_tmp_data += len(i)
                            self.client.send(i)
                            mget.update(i)
                            self.view_bar(len_tmp_data,file_size)
                        gfile_md5 = mget.hexdigest()
                        gserver_file_md5 = self.client.recv(4096).decode()
                        # print(gfile_md5,gserver_file_md5)

                    if gfile_md5 == gserver_file_md5: #对比md5
                        print('file:%s put   done ' % (self.command_input[-1]))
                    else:
                        print('file:%s check md5 value can not math' % (self.command_input[-1]))
            else:
                self.client.send(b'403') #收到403则用户在服务器端没有足够空间
                print('not enough space pls called administrators')
        else:
            print('connect to server has error ')

    def pwd(self):
        '''打印当前路径'''
        print(self.user_path)

    def cd(self):
        '''切换目录方法'''
        # print(self.user_path)
        self.cd_dic = {'action':'cd','cdpath':self.command_input[-1]}
        # print(self.cd_dic)
        self.into_dir = self.cd_dic['cdpath']
        if re.match('\w+',self.into_dir): #匹配目录 cd example
            # print('match cd example')
            self.client.send(str(self.cd_dic).encode()) #发送最新目录给server
            recv_server_chk = self.client.recv(4096) #server确认ok
            if recv_server_chk == b'200':
                # print('server path found') #更新client端显示的目录
                self.user_path = os.path.join(self.user_path, self.into_dir)
            else:
                print('server path has no found')
        elif re.match('..\.*',self.into_dir):# 匹配cd ../example  cd ..
            # print('match cd .. or cd ../example')
            if self.user_path == 'userdata/zhoutao': #判断是否已经是家目录了。
                print('403 access prement denly')
            else:
                into_dir_list = self.into_dir.split('../') #将../ 或则 ../dir1 分割成一个列表
                if len(into_dir_list) == 1: #只有cd ..命令
                    # print('only cd ..')
                    self.client.send(str(self.cd_dic).encode())
                    if self.client.recv(4096) == b'200': #等待服务器确认信息
                        # print('cd .. will be change user_path')
                        self.user_path = os.path.split(self.user_path)[0]
                elif len(into_dir_list) == 2: #匹配cd ../dir1
                    # print('only cd ../example')
                    self.client.send(str(self.cd_dic).encode())
                    if self.client.recv(4096) == b'200': #等待服务器确认信息
                        self.user_path = os.path.split(self.user_path)[0]
                        self.user_path = os.path.join(self.user_path,into_dir_list[1])
        elif re.match('~/\.*',self.into_dir): #匹配cd ~ ; cd ~/example
            # print('match cd ~ or cd ~/example')
            pass
        else:
            print('cd command error ')

    def ls(self):
        '''打印文件列表'''
        ls_dic = {'action':'ls'}
        self.client.send(str(ls_dic).encode()) #发送lsdic给服务器端
        ls_data = eval(self.client.recv(4096)) #接受到服务器发来的文件列表
        for i in ls_data: #循环打印文件列表
            print(i)

    @staticmethod
    def ftp_help():
        msg = '''
        【帮助信息】：
        可执行命令：
        ls：      查看目录内容
        cd：      切换目录
        get：     下载文件
        put：     上传文件
        help: 查看帮助文件
        '''
        print(msg)



