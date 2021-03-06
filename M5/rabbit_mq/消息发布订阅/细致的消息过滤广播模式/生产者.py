import pika

import sys

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()
channel.exchange_declare(exchange='topic_logs',type='topic')

routing_key = sys.argv[1] if len(sys.argv) > 1 else 'anonymous.info'
message = ' '.join(sys.argv[2:]) or 'Hello World!'
print(message)
channel.basic_publish(exchange='topic_logs',routing_key=routing_key,body=message)



connection.close()