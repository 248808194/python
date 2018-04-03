#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date:2017-04-26-13:32
# Python 3.5

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()


channel.queue_declare(queue='hello1',durable=True) #从哪个队列里面收消息


def callback(ch,method,properties,body): #标准格式待4个参数
    ch.basic_ack(delivery_tag=method.delivery_tag)
    print(body.upper())


channel.basic_qos(prefetch_count=1) # 消息公平发送
#置perfetch=1,意思就是告诉RabbitMQ在我这个消费者当前消息还没处理完的时候就不要再给我发新消息了。
channel.basic_consume(
    callback, #如果收到消息就调用callback方法去处理消息
    queue='hello1', #从哪个队列里面收消息
)

print('[*] Waiting for messages, To exit perss CTRL+C')
channel.start_consuming() #start一启动会一直收下去，没有消息则阻赛(卡住)住