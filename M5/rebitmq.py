#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date:2017-04-26-13:22
# Python 3.5

#producer
import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='127.0.0.1') #建立一个socket链接
)


channel = connection.channel() #声明一个频道(管道)

channel.queue_declare(queue='hello') #声明一个quue


channel.basic_publish(exchange = '',routing_key = 'hello', body = 'hello world') #routing_key = 上面声明的队列名字，将消息发送到这个queue里面

print('send hello world')
connection.close()