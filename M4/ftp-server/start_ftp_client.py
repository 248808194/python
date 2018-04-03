#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date:2017-03-06-16:07
# Python 3.5



import sys,os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
from ftp_client.core.socket_class import socket_client




def main():
    a = socket_client()

if __name__ == '__main__':
    main()