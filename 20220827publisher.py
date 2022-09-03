import pika, os

url = os.environ.get('CLOUDAMPQ_URL', 'ampq://guest@localhost:5672/')
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel() # start a channel

channel.exchange_declare('test_exchange') # declare exchange_declare
channel.queue_declare(queue='teste_queue') # declare queue
channel.queue_bind('teste_queue', 'test_exchange', 'tests') #create binding

#publish message 