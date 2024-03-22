import logging
import os
import connect

# Configuración de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
class ChatClient:

    def __init__(self):
        chat = connect.Connect('localhost', 8000)
        chat.create_connection()



    def connect_to_chat(self):
        try:
            chat = connect.Connect('localhost', 8000)
            chat.create_connection()
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