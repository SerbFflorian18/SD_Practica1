import grpc
from concurrent import futures
import time

# import the generated classes

import chatserver_pb2_grpc
import chatserver_pb2


# import grpc_files.chatserver_pb2_grpc

# import the original insultingServer.py
# from insulting_service import insulting_service


# create a class to define the server functions, derived from
# insultingServer_pb2_grpc.InsultingServiceServicer
class MessageServer(chatserver_pb2_grpc.ChatServerServicer):

    def __init__(self, client):
        self.client = client


    def SendMessage(self, message, context):

        #print("New Message dawg!" + message.message)
        self.client.save_message(message.message)

        response = chatserver_pb2.SendMessageResponse(message="hala")
        return response

    def ConnectToChat(self, request, context):
        print("Connected to " + str(request.sender))

        host, port = request.sender.split(":")

        self.client.connect_to_chat(host, int(port), True)

        response = chatserver_pb2.ConnectToChatResponse(accept=1)
        return response


def start_server(client):
    # create a gRPC server
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    # use the generated function `add_InsultingServiceServicer_to_server`
    # to add the defined class to the server
    chatserver_pb2_grpc.add_ChatServerServicer_to_server(
        MessageServer(client), server)

    # listen on port 50051
    print('Starting server. Listening on port 50051.')
    server.add_insecure_port('localhost:50051')
    server.start()

    # since server.start() will not block,
    # a sleep-loop is added to keep alive


