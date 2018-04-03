#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date:2017-02-28-14:40
# Python 3.5



#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date:2017-02-28-14:40
# Python 3.5

import os,socket



client = socket.socket()
client.connect(('127.0.0.1',9999,))

a = {'action':'get'}
client.send(str(a).encode())


filesize = os.stat('1.log').st_size
print(filesize)
tmp_size = 0
with open('123.log.new','wb') as f:
    while tmp_size < filesize:
        tmp_data = client.recv(4096)
        tmp_size += len(tmp_data)
        f.write(tmp_data)
        client.send(b'200')

print('file recv done')



