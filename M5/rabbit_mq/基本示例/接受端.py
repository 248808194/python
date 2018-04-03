import pika



connection = pika.BlockingConnection(pika.ConnectionParameters('localhost',5672))


channel = connection.channel()

channel.queue_declare(queue='hello')



def callback(ch,method,properties,body): #回调函数 四个参数，标准格式，写死
    print('ch is ',ch)
    print('method is',method)
    print('properties is ',properties)
    print('body is ',body)
    ch.basic_ack(delivery_tag=method.delivery_tag) # 告诉生成者消息处理完毕
    print(body.upper())



channel.basic_consume(
    callback, #收到消息就调用callback函数处理消息
    queue = 'hello',
)

channel.start_consuming()

