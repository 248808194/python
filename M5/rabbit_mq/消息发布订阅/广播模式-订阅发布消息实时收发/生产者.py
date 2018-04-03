import pika


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()

channel.exchange_declare(exchange='logs',type='fanout') # fanout指定类型

channel.basic_publish(exchange='logs',routing_key='',body='helloworld')

connection.close()
