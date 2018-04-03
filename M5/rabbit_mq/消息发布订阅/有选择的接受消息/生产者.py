import pika

import sys

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()

channel.exchange_declare(exchange='direct_logs',type='direct')

serverity = sys.argv[1] if len(sys.argv) > 1 else 'info' #重要程度级别，这里默认定义为 info

message = ' '.join(sys.argv[2:]) or 'hello world'

channel.basic_publish(exchange='direct_logs',routing_key=serverity,body=message)

connection.close()