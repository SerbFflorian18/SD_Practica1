import grpc
import chatserver_pb2
import chatserver_pb2_grpc
import nameserver_pb2
import nameserver_pb2_grpc
from concurrent import futures
import logging
import os

# Configuración de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configuración de variables de entorno
NAME_SERVER_HOST = os.getenv('NAME_SERVER_HOST', 'localhost')
NAME_SERVER_PORT = int(os.getenv('NAME_SERVER_PORT', 8000))

class ChatServerServicer(chatserver_pb2_grpc.ChatServerServicer):
    def __init__(self):
        self.name_server_channel = grpc.insecure_channel(f"{NAME_SERVER_HOST}:{NAME_SERVER_PORT}")
        self.name_server_stub = nameserver_pb2_grpc.NameServerStub(self.name_server_channel)

    def SendMessage(self, request, context):
        try:
            # Busca la dirección IP y el puerto del usuario receptor en el servidor de nombres
            lookup_response = self.name_server_stub.Lookup(nameserver_pb2.LookupRequest(username=request.receiver))
            if lookup_response.ip_address:
                # Enviar el mensaje al usuario receptor
                # Aquí implementarías la lógica para enviar el mensaje utilizando la dirección IP y el puerto obtenidos
                logger.info(f"Message sent to {request.receiver}.")
                return chatserver_pb2.SendMessageResponse(message="Message sent successfully.")
            else:
                logger.error(f"User {request.receiver} not found.")
                context.set_code(grpc.StatusCode.NOT_FOUND)
                context.set_details(f"User {request.receiver} not found.")
                return chatserver_pb2.SendMessageResponse(message=f"User {request.receiver} not found.")
        except grpc.RpcError as e:
            logger.error(f"Error sending message to {request.receiver}: {e}")
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(f"Error sending message to {request.receiver}: {e}")
            return chatserver_pb2.SendMessageResponse(message=f"Error sending message to {request.receiver}")

    def ReceiveMessage(self, request, context):
        def ReceiveMessage(self, request, context):
            try:
                # Implementar lógica para recibir mensajes para un usuario
                # Aquí podrías recuperar los mensajes de un usuario específico desde tu sistema de mensajería
                # Por ahora, devolvemos un mensaje estático indicando que los mensajes se recibieron correctamente
                return chatserver_pb2.ReceiveMessageResponse(message="Messages received successfully.")
            except Exception as e:
                logger.error(f"Failed to receive messages: {str(e)}")
                context.set_code(grpc.StatusCode.INTERNAL)
                context.set_details(f"Failed to receive messages: {str(e)}")
                return chatserver_pb2.ReceiveMessageResponse(message="Failed to receive messages.")

    def ConnectToChat(self, request, context):
        try:
            # Implementar lógica para conectar al chat
            # Por ahora, devolvemos un mensaje estático
            return chatserver_pb2.ConnectToChatResponse(message="Connected to chat successfully.")
        except Exception as e:
            logger.error(f"Failed to connect to chat: {str(e)}")
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(f"Failed to connect to chat: {str(e)}")
            return chatserver_pb2.ConnectToChatResponse(message="Failed to connect to chat.")

    def SubscribeToGroupChat(self, request, context):
        try:
            # Implementar lógica para suscribirse a un chat grupal
            # Por ahora, devolvemos un mensaje estático
            return chatserver_pb2.SubscribeToGroupChatResponse(message="Subscribed to group chat successfully.")
        except Exception as e:
            logger.error(f"Failed to subscribe to group chat: {str(e)}")
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(f"Failed to subscribe to group chat: {str(e)}")
            return chatserver_pb2.SubscribeToGroupChatResponse(message="Failed to subscribe to group chat.")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    chatserver_pb2_grpc.add_ChatServerServicer_to_server(ChatServerServicer(), server)
    server.add_insecure_port('localhost:8000')
    server.start()
    logger.info("Server started. Listening on port 8000.")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()