#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date:2017-04-26-13:22
# Python 3.5

#producer
import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='127.0.0.1'))

channel = connection.channel()

channel.exchange_declare(exchange='direct_logs',type='direct')

severity = sys.argv[1] if len(sys.argv) > 1 else 'info'
message = ' '.join(sys.argv[2:]) or 'Hello World!'
channel.basic_publish(
    exchange = 'direct_logs',
    routing_key = severity,
    body = message
)

print(" [x] Sent %r:%r" % (severity, message))
connection.close()