#_*_coding:utf-8_*_
__author__ = 'Alex Li'

import base64
import getpass
import os
import socket
import sys
import traceback
from paramiko.py3compat import input
from  modules import models
import datetime

import paramiko
try:
    import interactive
except ImportError:
    from . import interactive


def ssh_login(user_obj,bind_host_obj,mysql_engine,log_recording):
    # now, connect and use paramiko Client to negotiate SSH2 across the connection
    try: #尝试连接
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.WarningPolicy())
        print('*** Connecting...')
        #client.connect(hostname, port, username, password)
        client.connect(bind_host_obj.host.ip_addr, # 通过bind_host_obj获取到ｉｐ
                       bind_host_obj.host.port, # 通过bind_host_obj获取到 port
                       bind_host_obj.remoteuser.username,  # 通过bind_host_obj获取到 用户名
                       bind_host_obj.remoteuser.password, # 通过bind_host_obj获取到　密码
                       timeout=30)

        cmd_caches = []
        chan = client.invoke_shell() #调用shell
        print(repr(client.get_transport()))
        print('*** Here we go!\n')
        cmd_caches.append(models.AuditLog(user_id=user_obj.id,
                                          bind_host_id=bind_host_obj.id,
                                          action_type='login',
                                          date=datetime.datetime.now()
                                          )) #一行一条命令，以用户名，绑定主机ｉｄ　时间
        log_recording(user_obj,bind_host_obj,cmd_caches) #将命令写入到数据库下．
        interactive.interactive_shell(chan,user_obj,bind_host_obj,cmd_caches,log_recording)
        chan.close()
        client.close()

    except Exception as e:
        print('*** Caught exception: %s: %s' % (e.__class__, e))
        traceback.print_exc()
        try:
            client.close()
        except:
            pass
        sys.exit(1)