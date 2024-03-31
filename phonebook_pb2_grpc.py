# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
import phonebook_pb2 as phonebook__pb2


class PhoneBookServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AddEntry = channel.unary_unary(
                '/phonebook.PhoneBookService/AddEntry',
                request_serializer=phonebook__pb2.Entry.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.DeleteEntry = channel.unary_unary(
                '/phonebook.PhoneBookService/DeleteEntry',
                request_serializer=phonebook__pb2.Entry.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.SearchEntry = channel.unary_stream(
                '/phonebook.PhoneBookService/SearchEntry',
                request_serializer=phonebook__pb2.Entry.SerializeToString,
                response_deserializer=phonebook__pb2.Entry.FromString,
                )
        self.ViewEntry = channel.unary_unary(
                '/phonebook.PhoneBookService/ViewEntry',
                request_serializer=phonebook__pb2.Entry.SerializeToString,
                response_deserializer=phonebook__pb2.Entry.FromString,
                )


class PhoneBookServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def AddEntry(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteEntry(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SearchEntry(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ViewEntry(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PhoneBookServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'AddEntry': grpc.unary_unary_rpc_method_handler(
                    servicer.AddEntry,
                    request_deserializer=phonebook__pb2.Entry.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'DeleteEntry': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteEntry,
                    request_deserializer=phonebook__pb2.Entry.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'SearchEntry': grpc.unary_stream_rpc_method_handler(
                    servicer.SearchEntry,
                    request_deserializer=phonebook__pb2.Entry.FromString,
                    response_serializer=phonebook__pb2.Entry.SerializeToString,
            ),
            'ViewEntry': grpc.unary_unary_rpc_method_handler(
                    servicer.ViewEntry,
                    request_deserializer=phonebook__pb2.Entry.FromString,
                    response_serializer=phonebook__pb2.Entry.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'phonebook.PhoneBookService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class PhoneBookService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def AddEntry(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/phonebook.PhoneBookService/AddEntry',
            phonebook__pb2.Entry.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteEntry(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/phonebook.PhoneBookService/DeleteEntry',
            phonebook__pb2.Entry.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SearchEntry(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/phonebook.PhoneBookService/SearchEntry',
            phonebook__pb2.Entry.SerializeToString,
            phonebook__pb2.Entry.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ViewEntry(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/phonebook.PhoneBookService/ViewEntry',
            phonebook__pb2.Entry.SerializeToString,
            phonebook__pb2.Entry.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)