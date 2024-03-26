import grpc
import chatserver_pb2_grpc
class Connect:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.channel = ''
        self.stub = ''

    def create_connection(self):
        self.channel = grpc.insecure_channel(self.host + ":" + str(self.port))
        self.stub = chatserver_pb2_grpc.ChatServerStub(self.channel)
