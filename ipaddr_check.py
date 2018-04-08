#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date:2018-04-08-13:49
# Python 3.6

import os
import sys
import smtplib
import multiping
import time
import platform
import subprocess
from multiping import MultiPing
import smtplib
import threading
import pyping
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText



class ipaddr_checl(object):

    def __init__(self, file):
        self.file = file
        if platform.platform().startswith('Windows'):
            self.traccommand = 'tracert -d -w 250 -h 4'
        elif platform.platform().startswith('Linux'):
            self.traccommand = 'traceroute -m 12 -n -w 0.5'

    @staticmethod
    def check_result(line):
        with open('ip_check_failed.result','a+') as f1:
            f1.write(line)

    @staticmethod
    def read_result():
        with open('ip_check_failed.result','rb') as f1:
            result = f1.read()
        return  result

    def return_iplist(self):
        with open(self.file,'r') as f1:
            ip_list_lines = f1.readlines()
        return ip_list_lines

    def mail_method(self,content):
        msg_from = '248808194@qq.com'
        passwd = '**************' #should be security token not password
        msg_to = 'zhoutao@zhoutao.name'
        subject = "iplist"
        msg = MIMEText(content)
        msg['Subject'] = subject
        msg['From'] = msg_from
        msg['To'] = msg_to
        # txtpart = MIMEApplication(open('ip_check_failed.result', 'rb').read())
        # txtpart.add_header('Content-Disposition', 'attachment', filename='ip_check_failed.result')
        # msg.attach(txtpart)
        try:
            s = smtplib.SMTP_SSL("smtp.qq.com", 465)
            s.login(msg_from, passwd)
            s.sendmail(msg_from, msg_to, msg.as_string())
            print("success")
        except smtplib.SMTPException as e:
            print(e)
        finally:
            s.quit()

    def ping_method(self, single_ip):
        r = pyping.ping(single_ip)
        if r.ret_code == 0:
            return True
        elif r.ret_code == 1:
            return single_ip

    def tracert_method(self, single_ip):
	pi = subprocess.Popen('%s %s' %(self.traccommand,single_ip),shell=True,stdout=subprocess.PIPE)
	aaa = pi.stdout.read()
        return aaa

def foo(program,i):
    i = i.strip()
    check_ip_status = program.ping_method(i)
    print(i,check_ip_status)
    if check_ip_status != 'True': #ip address  Unreachable
        # program.tracert_method(i)
        context = program.tracert_method(i)
        ipaddr_checl.check_result(context)

def main():
    t_objs = []
    program = ipaddr_checl('ip.txt')
    for i in program.return_iplist():
        i = i.strip()
        t = threading.Thread(target=foo, args=(program,i,))
        t.start()
        t_objs.append(t)
    for tt in t_objs:
        tt.join()

    result = ipaddr_checl.read_result()
    program.mail_method(result)



if __name__ == '__main__':
    main()
