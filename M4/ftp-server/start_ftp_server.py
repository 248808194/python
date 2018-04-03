#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date:2017-03-06-15:58
# Python 3.5

import socketserver,json,os,sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
from ftp_server.core.mysocketserver import MYsocketserver

IP_PORT = ("127.0.0.1",9999)


if __name__ == "__main__":
    server = socketserver.ThreadingTCPServer(IP_PORT,MYsocketserver)
    server.serve_forever()