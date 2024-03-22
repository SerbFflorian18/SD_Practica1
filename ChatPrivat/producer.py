import pika

connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.queue_declare(queue='chat')

message = "Hello, this is my first message"

channel.basic_publish(exchange='chat', routing_key='chat', body=message)

print(f"Sent message: {message}")

connection.close()