# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
import insultingServer_pb2 as insultingServer__pb2


class InsultingServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetInsults = channel.unary_unary(
                '/InsultingService/GetInsults',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=insultingServer__pb2.Insults.FromString,
                )
        self.AddInsult = channel.unary_unary(
                '/InsultingService/AddInsult',
                request_serializer=insultingServer__pb2.Insult.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.InsultMe = channel.unary_unary(
                '/InsultingService/InsultMe',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=insultingServer__pb2.InsultName.FromString,
                )
        self.GetSeverity = channel.unary_unary(
                '/InsultingService/GetSeverity',
                request_serializer=insultingServer__pb2.InsultName.SerializeToString,
                response_deserializer=insultingServer__pb2.Severity.FromString,
                )


class InsultingServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetInsults(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddInsult(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def InsultMe(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetSeverity(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_InsultingServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetInsults': grpc.unary_unary_rpc_method_handler(
                    servicer.GetInsults,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=insultingServer__pb2.Insults.SerializeToString,
            ),
            'AddInsult': grpc.unary_unary_rpc_method_handler(
                    servicer.AddInsult,
                    request_deserializer=insultingServer__pb2.Insult.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'InsultMe': grpc.unary_unary_rpc_method_handler(
                    servicer.InsultMe,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=insultingServer__pb2.InsultName.SerializeToString,
            ),
            'GetSeverity': grpc.unary_unary_rpc_method_handler(
                    servicer.GetSeverity,
                    request_deserializer=insultingServer__pb2.InsultName.FromString,
                    response_serializer=insultingServer__pb2.Severity.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'InsultingService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class InsultingService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetInsults(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/InsultingService/GetInsults',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            insultingServer__pb2.Insults.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddInsult(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/InsultingService/AddInsult',
            insultingServer__pb2.Insult.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def InsultMe(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/InsultingService/InsultMe',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            insultingServer__pb2.InsultName.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetSeverity(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/InsultingService/GetSeverity',
            insultingServer__pb2.InsultName.SerializeToString,
            insultingServer__pb2.Severity.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
