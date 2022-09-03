import pika, os

url = os.environ.get('CLOUDAMPQ_URL, ####### COPIAR DO SEND
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel() #start channel
channel.queue_declare(queue='test_queue')

def callback(ch, method, properties, body):
    print(' [x] Received ' + str(body))
    
    channel.basic_consume(
    'test_queue',
    callback,
    auto_ack=True)
    
    print(' [*] Esperando mensagens:')
    channel.start_consuming()
    connection.close()