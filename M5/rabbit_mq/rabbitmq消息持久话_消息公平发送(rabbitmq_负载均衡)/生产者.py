import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()

channel.queue_declare(queue='hello1',durable=True) #durable队列持久话

channel.basic_publish(
    exchange='',
    routing_key = 'hello1',
    body ='hello world',
    properties = pika.BasicProperties(delivery_mode=2) # 队列中的消息在持久话
)


connection.close()



