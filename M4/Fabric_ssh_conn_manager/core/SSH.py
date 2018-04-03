#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date:2017-02-09-09:23
# Python 3.5


import paramiko
import os,sys,time
import subprocess


class SSH(object):

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    def __init__(self,tuple_args):

        self.host = tuple_args[0]
        self.port = tuple_args[1]
        self.username = tuple_args[2]
        self.password = tuple_args[3]
    def comm(self,command):
        '''执行命令方法'''
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(hostname=self.host,port=self.port,username=self.username,password=self.password)
        self.stdin,self.stdout,self.shderr = self.ssh.exec_command(command,timeout=3,get_pty=True)
        # print(self.stdout,self.shderr)
        self.out = str(self.stdout.read(),encoding='utf8')
        # print(self.out)
        print(self.host,'\n',self.out)
        self.ssh.close()



    def upload_download_init(self):
        '''初始化上传下载方法'''
        self.t = paramiko.Transport((self.host,self.port)) #这里是一个元祖格式
        self.t.connect(username=self.username,password=self.password)
        self.sftp = paramiko.SFTPClient.from_transport(self.t)
        return self.sftp
    #
    #
    def upload(self,files,remotepath):
        '''上传方法'''
        upload_sftp = self.upload_download_init()
        upload_sftp.put(files,remotepath)
        upload_sftp.close()


    def download(self,files,localpath):
        '''下载方法'''
        download_sftp = self.upload_download_init()
        download_sftp.get(files,localpath)
        download_sftp.close()


# server1 = SSH('180.153.238.109',23432,'root')
#
# server1.comm
# # server1.download('/tmp/test.txt','/tmp/test.txt')
# # server1.upload('/tmp/test.txt','/tmp/123test.txt')


