import grpc
import nameserver_pb2
import nameserver_pb2_grpc
import redis
from concurrent import futures
import logging
import os

# Configuración de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configuración de variables de entorno
REDIS_HOST = os.getenv('REDIS_HOST', 'localhost')
REDIS_PORT = int(os.getenv('REDIS_PORT', 6379))

class NameServerServicer(nameserver_pb2_grpc.NameServerServicer):
    def __init__(self):
        try:
            # Conexión a Redis
            self.redis_client = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=0)
            logger.info("Connected to Redis successfully.")
        except Exception as e:
            logger.error(f"Failed to connect to Redis: {str(e)}")
            raise

    def Register(self, request, context):
        try:
            # Registra la dirección IP y el puerto del usuario en Redis
            self.redis_client.set(request.username, f"{request.ip_address}:{request.port}")
            logger.info(f"Registered {request.username} successfully.")
            return nameserver_pb2.RegisterResponse(message="Registered successfully.")
        except Exception as e:
            logger.error(f"Failed to register {request.username}: {str(e)}")
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(f"Failed to register {request.username}: {str(e)}")
            return nameserver_pb2.RegisterResponse(message=f"Failed to register {request.username}")

    def Lookup(self, request, context):
        try:
            # Busca la dirección IP y el puerto del usuario en Redis
            connection_info = self.redis_client.get(request.username)
            if connection_info:
                ip_address, port = connection_info.decode().split(':')
                logger.info(f"Lookup: {request.username} found at {ip_address}:{port}")
                return nameserver_pb2.LookupResponse(ip_address=ip_address, port=int(port), message="User found.")
            else:
                logger.info(f"Lookup: {request.username} not found.")
                return nameserver_pb2.LookupResponse(message="User not found.")
        except Exception as e:
            logger.error(f"Failed to lookup {request.username}: {str(e)}")
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(f"Failed to lookup {request.username}: {str(e)}")
            return nameserver_pb2.LookupResponse(message=f"Failed to lookup {request.username}")

    def DiscoverChats(self, request, context):
        try:
            # Implementar lógica para descubrir chats
            # Por ahora, devolvemos una lista vacía
            return nameserver_pb2.DiscoverChatsResponse(chats=[])
        except Exception as e:
            logger.error(f"Failed to discover chats: {str(e)}")
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(f"Failed to discover chats: {str(e)}")
            return nameserver_pb2.DiscoverChatsResponse(chats=[])

    def JoinInsultChannel(self, request, context):
        try:
            # Implementar lógica para unirse al canal de insultos
            # Por ahora, devolvemos un mensaje estático
            return nameserver_pb2.JoinInsultChannelResponse(message="Joined insult channel successfully.")
        except Exception as e:
            logger.error(f"Failed to join insult channel: {str(e)}")
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(f"Failed to join insult channel: {str(e)}")
            return nameserver_pb2.JoinInsultChannelResponse(message="Failed to join insult channel")


def serve():
    try:
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        nameserver_pb2_grpc.add_NameServerServicer_to_server(NameServerServicer(), server)
        server.add_insecure_port('[::]:8000')
        server.start()
        logger.info("Server started. Listening on port 8000.")
        server.wait_for_termination()
    except Exception as e:
        logger.error(f"Failed to start server_V0: {str(e)}")
        raise

if __name__ == '__main__':
    serve()