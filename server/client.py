import grpc
import chatserver_pb2
import chatserver_pb2_grpc
import nameserver_pb2
import nameserver_pb2_grpc
import logging
import os

# Configuración de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configuración de variables de entorno
NAME_SERVER_HOST = os.getenv('NAME_SERVER_HOST', 'localhost')
NAME_SERVER_PORT = int(os.getenv('NAME_SERVER_PORT', 8000))

class ChatClient:
    def __init__(self):
        self.username = input("Enter your username: ")
        self.name_server_channel = grpc.insecure_channel(f"{NAME_SERVER_HOST}:{NAME_SERVER_PORT}")
        self.name_server_stub = nameserver_pb2_grpc.NameServerStub(self.name_server_channel)

    def connect_to_chat(self):
        try:
            # Implementar lógica para conectar al chat
            # Por ahora, devolvemos un mensaje estático
            logger.info("Connected to chat successfully.")
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

if __name__ == '__main__':
    client = ChatClient()
    client.show_options()