import pika,sys


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs',type='direct')

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue


print(sys.argv)

# 获取运行脚本所有的参数
severites = sys.argv[1:]
print(severites)
if not severites:
    sys.stderr.write("Usage: %s [info] [warning] [error]\n" % sys.argv[0])
    sys.exit(1)



for severity in severites:
    channel.queue_bind(exchange='direct_logs',queue = queue_name,routing_key=severity)

print(' [*] Waiting for logs. To exit press CTRL+C')
def callback(ch,method,properties,body):
    print(method.routing_key, body)



channel.basic_consume(callback,queue=queue_name,no_ack=True)

channel.start_consuming()
