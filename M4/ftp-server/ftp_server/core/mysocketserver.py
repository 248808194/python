#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date:2017-02-28-14:40
# Python 3.5

import socketserver,json,os,sys,re,hashlib
from os.path import join, getsize
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class MYsocketserver(socketserver.BaseRequestHandler):


    def handle(self):
        '''
        接受客户端传入的字典，先解析字典判断动作类型
        通过动作类型来反射出方法
        :return:
        '''
        self.m = self.hashsecurity()
        while True:
            recv_msg = self.request.recv(4096)
            if not recv_msg:
                print('empoty msg ')
                break
            recv_msg = str(recv_msg,encoding='utf8')
            self.recv_msg_dict = eval(recv_msg)
            print(self.recv_msg_dict)
            action = self.recv_msg_dict.get('action')
            if hasattr(self,'%s'%(action)):
                print('hasattr')
                func = getattr(self,'%s'%action)
                func()



    def du(self):
        '''查看当前用户磁盘文件总大小'''
        allfile_size = 0
        print('in du self.userbase home',self.user_base_home)
        user_dir = os.path.join(self.user_base_home)
        print(user_dir)
        for roots, dirs, files in os.walk(user_dir):
            allfile_size += sum([getsize(join(roots, name)) for name in files])
        return allfile_size

    def hashsecurity(self):
        '''hashlib md5 加密方法'''
        obj = hashlib.md5()
        return obj

    def login(self):
        '''
        登录验证方法，
        客户端传入用户名密码，来和json文件反序列化生成的db_dict做对比，如果失败返回403给客户端
        :return:
        '''
        print('excluting login func')

        dbfile = os.path.join(BASE_DIR,'conf','userdb.json') #服务器端json文件绝对路径
        print(dbfile)

        if os.path.exists(dbfile):
            db_dict = json.load(open(dbfile,'r')) #json反序列化用户配置文件
            in_comming_username = self.recv_msg_dict['username']
            in_comming_password = self.recv_msg_dict['password']
            self.user_base_home = os.path.join(BASE_DIR, 'userdata', in_comming_username)
            self.user_quota = int(db_dict[in_comming_username]['quota'])
            if db_dict[in_comming_username] and  db_dict[in_comming_username]['password'] == in_comming_password: #检查用户名密码
                self.user_path = str(os.path.join('userdata',in_comming_username))
                self.request.send(self.user_path.encode()) #验证成功发送用户家目录给客户端 Example: userdata/zhoutao
            else:
                self.request.send(b'403') #验证不通过返回给客户端403错误代码
        else:
            self.request.send(b'403')


    def get(self):
        '''服务器端下载方法'''
        mget = hashlib.md5()
        filename = self.recv_msg_dict['filename'] #从客户端传来的字典获取客户端需要下载文件名
        print('recv get filename is ',filename)
        server_file_name = os.path.join(BASE_DIR,filename) #拼凑出文件abs path
        print(server_file_name)
        if os.path.isfile(server_file_name): #检查文件是否存在
            file_total_size = str(os.stat(server_file_name).st_size) #获取文件大小
            self.request.send(file_total_size.encode()) #发送服务器端文件大小给客户端
            file_tmp_size = self.request.recv(4096).decode() #客户端会检测如果文件未传送完成，获取从客户端传来的文件大小，如果文件未发送则接受到0
            print('file_tmp1111_szie ',file_tmp_size)
            file_tmp_size = int(file_tmp_size)
            if file_tmp_size == 1000: #如果客户端传输完成文件则服务器端会接受到1000
                return False
            print('recv from client file tmp size is ',file_tmp_size)
            with open(server_file_name,'rb') as f: #打开发送文件循环的发送给客户端
                print('in with seek size is ',file_tmp_size)
                f.seek(file_tmp_size) # #文件偏移量
                for i in f:
                    print(len(i))
                    self.request.sendall(i)
                    mget.update(i) #更新MD5值
            print('file send done')
            file_md5 = mget.hexdigest()
            print(file_md5)
            self.request.send(file_md5.encode()) #发送服务器端MD5校验码
        else:
            self.request.send(b'404') #file not found


    def put(self):
        '''服务器端下载方法'''
        self.all_used_space = int(self.du()) #在服务器端上传文件之前先拿到用户目录下所有文件大小
        mput = hashlib.md5() #初始化一个md5对象
        filename = os.path.join(BASE_DIR,self.recv_msg_dict['filename']) #从客户端put字典获取到文件名，拼凑出服务器端绝对路径
        print(filename)
        free_space =  str(self.user_quota - self.all_used_space) #用户空间剩余大小
        # self.request.send(free_space.encode()) #发送空闲空间给客户端
        du_dic = {'200':free_space} #生成剩余空间字典
        print('du dic is ',du_dic)
        self.request.sendall(str(du_dic).encode()) #发送剩余空间大小给客户端
        file_client_size = int(self.request.recv(4096))
        if file_client_size == 403: # 客户端计算出传入文件大于剩余空间大小则返回403，告诉客户端磁盘空间不够
            print('not enough space')
        else:
            print('put file_client_size',file_client_size)
            self.request.sendall(b'R') # 空间够用，则发送R关键字，客户端开始循环发送文件给服务器端
            print(file_client_size,type(file_client_size))
            tmp_file_size = 0
            with open(filename, 'wb') as f: #服务器端开始写入文件，并且计算出MD5
                print('in open file')
                while tmp_file_size < file_client_size:
                    if file_client_size - tmp_file_size > 4096:
                        size = 4096
                    else:
                        size = file_client_size - tmp_file_size
                    tmp_data = self.request.recv(size)
                    tmp_file_size += len(tmp_data)
                    f.write(tmp_data)
                    mput.update(tmp_data)

                else:
                    file_md5 = mput.hexdigest()
                    self.request.send(file_md5.encode()) #文件传输完成发送MD5给客户端
                    print('file send done')


    def pwd(self):
        '''打印当前的路径发送给客户端'''
        current_path = self.user_path
        print('current path is ',current_path)
        self.request.send(current_path.encode())

    def chk_dir(self):
        '''配合cd命令用于检查用户cd的目录是否存在'''
        if os.path.exists(self.user_base_home):
            self.request.send(b'200')
            return True
        else:
            self.request.send(b'404')
            return  False


    def cd(self):
        '''
        服务器端cd方法
        通过接受客户端发来的cd dir 只在服务器端更新当前目录并不发送给客户端
        :return:
        '''
        print('by default server user path  is',self.user_base_home)
        old_path = self.user_base_home #初始化用户家目录
        print('old path is ',old_path)
        cdpath = self.recv_msg_dict['cdpath'] #从客户端传来的cd字典拿到用户需要进入的目录
        print('cdpath from dict is ',cdpath)
        if re.match('\w+', cdpath):  # 匹配目录 cd example
            print('in cd example before dirname is :',self.user_base_home)
            old_path = self.user_base_home
            print('in first math old path is ',old_path)
            self.user_base_home = os.path.join(self.user_base_home,cdpath) #更新目录
            if self.chk_dir():# 如果目录存在
                print('in cd example after dirname is :',self.user_base_home)
            else:
                self.user_base_home = old_path
        elif re.match('..\.*',cdpath): # 匹配 cd .. 或则cd ../example
            tmpcd_path_list = cdpath.split('../') #以../ 来分割传入的目录
            if len(tmpcd_path_list) == 1: # #只匹配cd ..
                print('only math cd ..')
                if self.chk_dir(): #查看目录是否存在
                    self.user_base_home = os.path.split(self.user_base_home)[0]
                    print('after cd .. only current dir is ',self.user_base_home)
                else:
                    self.user_base_home = old_path #目录不存在还原原来的目录结构

            else:
                old_path = self.user_base_home #匹配cd ../dir
                print('before cd ../example  only current dir is ',self.user_base_home)
                print('tmpcdpathlist is ',tmpcd_path_list)
                if self.chk_dir(): #如果目录存在则更新目录
                    self.user_base_home = os.path.split(self.user_base_home)[0]
                    self.user_base_home = os.path.join(self.user_base_home,tmpcd_path_list[-1])
                    print('after cd ../example current dir is',self.user_base_home)
                else:
                    self.user_base_home = old_path #目录不存在服务器端修改灰原来的目录

    def ls(self):
        '''
        打印当前目录结构发送给客户端
        :return:
        '''
        print(self.user_base_home)
        self.request.send(str(os.listdir(self.user_base_home)).encode())

