import pika


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()

channel.exchange_declare(exchange='logs',type='fanout') # fanout指定类型


result = channel.queue_declare(exclusive=True)#不指定queue名字,rabbit会随机分配一个名字,exclusive=True会在使用此queue的消费者断开后,自动将queue删除

queue_name = result.method.queue

channel.queue_bind(exchange='logs',queue=queue_name)

def callback(ch,method,properties,body):
    print(body.upper())



channel.basic_consume(callback,queue=queue_name,no_ack=True)

channel.start_consuming()
