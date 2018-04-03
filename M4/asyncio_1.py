#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date:2017-03-30-10:14
# Python 3.5

import asyncio,threading
#
# @asyncio.coroutine
# def hello():
#     print('hello world ',threading.current_thread())
#     yield from asyncio.sleep(1)
#     print('hello again',threading.current_thread())
#
# loop = asyncio.get_event_loop()
# task = [hello(),hello()]
#
# loop.run_until_complete(asyncio.wait(task))
# loop.close()

#
# @asyncio.coroutine
# def hello():
#     print('hello world')
#     print('hello again!')
#
#
# loop = asyncio.get_event_loop()
#
# loop.run_until_complete(hello())
# loop.close()


# @asyncio.coroutine
# def wget(host):
#     print('wget %s'%host)
#     connect = asyncio.open_connection(host,80)
#     reader,writer = yield from connect
#     print(reader,writer)
#     header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
#     writer.write(header.encode('utf-8'))
#     yield from writer.drain()
#     while True:
#         line = yield from reader.readline()
#         if line == b'\r\n':
#             break
#         print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
#
#     writer.close()
#
#
# loop = asyncio.get_event_loop()
# tasks = [wget(host) for host in  ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()


#
# import asyncio
#
#
# async def foo(x):
#     y = x
#     print(x+y)
#
#
# loop = asyncio.get_event_loop()
# tasks = [
#     foo(1),
#     foo(2),
#     foo(3),
#     foo(14),
#     foo(15),
#     foo(16),
#     foo(17),
#     foo(18),
#     foo(19),
#     foo(10),
#     foo(11),
#     foo(11),
#     foo(11),
#     foo(11),
# ]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()

# async def compute(x, y):
#     print("Compute %s + %s ..." % (x, y))
#     # await asyncio.sleep(10.0)
#     return x + y
#
#
# async def print_sum(x, y):
#     result = await compute(x, y)
#     print("%s + %s = %s" % (x, y, result))
#
#
# loop = asyncio.get_event_loop()
# tasks = [print_sum(1, 2), print_sum(3, 4)]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()

# from gevent import monkey
# monkey.patch_all()
#
# import requests
# from gevent.pool import Pool
#
#
# def download(url):
#     return urllib2.urlopen(url).read()
#
#
# if __name__ == '__main__':
#     urls = ['http://httpbin.org/get'] * 100
#     pool = Pool(20)
#     print pool.map(download, urls)

# import asyncio
# import aiohttp
