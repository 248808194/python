#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date:2017-03-06-15:58
# Python 3.5

import socketserver

from ftp_server.mysocketserver import MYsocketserver
IP_PORT = ("127.0.0.1",9999)


if __name__ == "__main__":
    server = socketserver.ThreadingTCPServer(IP_PORT,MYsocketserver)
    server.serve_forever()