#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date:2017-03-21-15:58
# Python 3.5

import  paramiko


ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='localhost',password='1',username='zt',port=22)

stdin ,stdout ,stderr = ssh.exec_command('dfs')

if not stdout:
    result = stderr.read()
    print(result)
else:

    result = stdout.read()
print(result.decode())

