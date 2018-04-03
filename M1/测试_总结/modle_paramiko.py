#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date:2016/12/9 0009 16:25
#file: modle_paramiko.py
# Python 3.5



import os,sys
import paramiko
key = "id_rsa"
key = paramiko.RSAKey.from_private_key_file(key)
t = paramiko.Transport(('180.153.238.109',23432))
t.connect(username='root',pkey=key)
sftp = paramiko.SFTPClient.from_transport(t)
sftp.put('t.json','/tmp/t.json')
t.close()


import os,sys

t = paramiko.Transport(('180.153.238.109',23432))
t.connect(username='root',pkey=key)
sftp = paramiko.SFTPClient.from_transport(t)
sftp.get('/tmp/t.json','123.json')
t.close()