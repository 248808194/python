import pika
import time

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def on_request(ch,method,props,body):
    n= int(body)
    aa = fib(n)
    print('FIB VALUES is',aa)
    ch.basic_publish(
        exchange='',
        routing_key = props.reply_to,
        properties = pika.BasicProperties(correlation_id=props.correlation_id),
        body = str(aa)
    )
    ch.basic_ack(delivery_tag=method.delivery_tag)

if __name__ == '__main__':
    connection = pika.BlockingConnection(pika.ConnectionParameters(
            host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='rpc_queue')  # 声明一个rpc_queue ,
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(on_request,queue='rpc_queue') # 从rpc_queue接受消息，一旦收到消息就回调on_requests函数
    print('[x] Awaiting PRC requests')
    channel.start_consuming()



