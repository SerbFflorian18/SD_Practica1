import logging
import os
import time
from concurrent import futures

import grpc

import connect
import chatserver_pb2
import chatserver_pb2_grpc

from message_server import start_server, MessageServer

# Configuración de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ChatClient:

    def __init__(self, mine):
        self.mine = mine
        self.chat = None
        self.connected = False
        self.message = ""
        self.new_message = False

    def connect_to_chat(self, host, port, second_con):
        try:
            self.chat = connect.Connect(host, port)
            self.chat.create_connection()
            self.connected = True
            if not second_con:
                req = chatserver_pb2.ConnectToChatRequest(sender=self.mine, receiver=host + ":" + str(port))
                res = self.chat.stub.ConnectToChat(req)


                if int(res.accept) == 1:
                    print("Request accepted")
                    logger.info("Connected to chat")
                else:
                    print("Request denied")
                    logger.error(f"Request denied to connect")
        except Exception as e:
            logger.error(f"Failed to connect to chat: {str(e)}")

    def send_message(self, content):
        try:
            message = chatserver_pb2.SendMessageRequest(sender="localhost:55", receiver="localhost:22", message=content)
            res = self.chat.stub.SendMessage(message)
            #print("Response : " + res.message)
            #logger.info("Message sent sucessfully")
        except Exception as e:
            logger.error(f"Failed to connect to chat: {str(e)}")

    def listen_to_messages(self):
        try:
            start_server(self.save_message)
        except Exception as e:
            logger.error(f"Failed to connect to chat: {str(e)}")

    def subscribe_to_group_chat(self):
        try:
            # Implementar lógica para suscribirse a un chat grupal
            # Por ahora, devolvemos un mensaje estático
            logger.info("Subscribed to group chat successfully.")
        except Exception as e:
            logger.error(f"Failed to subscribe to group chat: {str(e)}")

    def discover_chats(self):
        try:
            # Implementar lógica para descubrir chats
            # Por ahora, devolvemos una lista vacía
            logger.info("Discovered chats successfully.")
        except Exception as e:
            logger.error(f"Failed to discover chats: {str(e)}")

    def join_insult_channel(self):
        try:
            # Implementar lógica para unirse al canal de insultos
            # Por ahora, devolvemos un mensaje estático
            logger.info("Joined insult channel successfully.")
        except Exception as e:
            logger.error(f"Failed to join insult channel: {str(e)}")

    def show_options(self):
        try:
            # Implementar lógica para mostrar las opciones del cliente y manejar la entrada del usuario
            print("Options:")
            print("1. Connect to chat")
            print("2. Subscribe to group chat")
            print("3. Discover chats")
            print("4. Join insult channel")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.connect_to_chat()
            elif choice == '2':
                self.subscribe_to_group_chat()
            elif choice == '3':
                self.discover_chats()
            elif choice == '4':
                self.join_insult_channel()
            else:
                logger.error("Invalid choice. Please enter a valid option.")

        except Exception as e:
            logger.error(f"Failed to show options: {str(e)}")

    def save_message(self, message):
        self.message = message
        self.new_message = True

if __name__ == '__main__':
    port = str(input("Enter your port:"))
    current = 'localhost:' + port
    client = ChatClient(current)
    # client.show_options()





    # create a gRPC server
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    # use the generated function `add_InsultingServiceServicer_to_server`
    # to add the defined class to the server
    chatserver_pb2_grpc.add_ChatServerServicer_to_server(
        MessageServer(client), server)

    # listen on port 50051
    print('Starting server. Listening on port ' + port)
    server.add_insecure_port(current)
    server.start()

    #

    # since server.start() will not block,
    # a sleep-loop is added to keep alive
    try:
        while True:

            if client.connected:
                print("Enter a message: ")
                msg = input()
                client.send_message(msg)
                if client.new_message:
                    print(client.message)
                    client.new_message = False
            else:
                con = int(input("Enter port to connect:"))
                if con != 0:
                    client.connect_to_chat("localhost", con, False)
            time.sleep(1)

    except KeyboardInterrupt:
        server.stop()


