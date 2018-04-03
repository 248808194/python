#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date:2017-02-28-14:36
# Python 3.5

#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date = '2016/8/4=%time'
# Python 3.5

import socketserver,json
IP_PORT = ("127.0.0.1",9999)
class MYsocketserver(socketserver.BaseRequestHandler):
    pass



if __name__ == "__main__":
    server = socketserver.ThreadingTCPServer(IP_PORT,MYsocketserver)
    server.serve_forever()
