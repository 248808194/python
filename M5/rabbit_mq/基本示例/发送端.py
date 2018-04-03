
#参考地址
#http://blog.csdn.net/fgf00/article/details/52872730
import  pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost',5672)) #建立一个rabbitmq链接

channel = connection.channel() #建立一个频道

channel.queue_declare(queue='hello') # 在刚刚建立的频道中放入一个队列queue


channel.basic_publish(
    exchange = '',
    routing_key = 'hello',
    body = 'hello world'
)


connection.close()