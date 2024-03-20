import pika

connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.queue_declare(queue='ChatPrivat')

message = "Hello, this is my first message"

channel.basic_publish(exchange='', routing_key='ChatPrivat', body=message)

print(f"Sent message: {message}")

connection.close()