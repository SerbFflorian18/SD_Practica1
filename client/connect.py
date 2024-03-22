import grpc
class Connect:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.channel = ''

    def create_connection(self):
        self.channel = grpc.insecure_channel(str(self.host + ":" + self.port))
