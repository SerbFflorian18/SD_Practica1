# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chatserver.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10\x63hatserver.proto\x12\x06server\"G\n\x12SendMessageRequest\x12\x0e\n\x06sender\x18\x01 \x01(\t\x12\x10\n\x08receiver\x18\x02 \x01(\t\x12\x0f\n\x07message\x18\x03 \x01(\t\"&\n\x13SendMessageResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\")\n\x15ReceiveMessageRequest\x12\x10\n\x08receiver\x18\x01 \x01(\t\"~\n\x16ReceiveMessageResponse\x12\x38\n\x08messages\x18\x01 \x03(\x0b\x32&.server_V0.ReceiveMessageResponse.Message\x1a*\n\x07Message\x12\x0e\n\x06sender\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t\"\x16\n\x14\x43onnectToChatRequest\"(\n\x15\x43onnectToChatResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x1d\n\x1bSubscribeToGroupChatRequest\"/\n\x1cSubscribeToGroupChatResponse\x12\x0f\n\x07message\x18\x01 \x01(\t2\xde\x02\n\nChatServer\x12H\n\x0bSendMessage\x12\x1a.server_V0.SendMessageRequest\x1a\x1b.server_V0.SendMessageResponse\"\x00\x12Q\n\x0eReceiveMessage\x12\x1d.server_V0.ReceiveMessageRequest\x1a\x1e.server_V0.ReceiveMessageResponse\"\x00\x12N\n\rConnectToChat\x12\x1c.server_V0.ConnectToChatRequest\x1a\x1d.server_V0.ConnectToChatResponse\"\x00\x12\x63\n\x14SubscribeToGroupChat\x12#.server_V0.SubscribeToGroupChatRequest\x1a$.server_V0.SubscribeToGroupChatResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'chatserver_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_SENDMESSAGEREQUEST']._serialized_start=28
  _globals['_SENDMESSAGEREQUEST']._serialized_end=99
  _globals['_SENDMESSAGERESPONSE']._serialized_start=101
  _globals['_SENDMESSAGERESPONSE']._serialized_end=139
  _globals['_RECEIVEMESSAGEREQUEST']._serialized_start=141
  _globals['_RECEIVEMESSAGEREQUEST']._serialized_end=182
  _globals['_RECEIVEMESSAGERESPONSE']._serialized_start=184
  _globals['_RECEIVEMESSAGERESPONSE']._serialized_end=310
  _globals['_RECEIVEMESSAGERESPONSE_MESSAGE']._serialized_start=268
  _globals['_RECEIVEMESSAGERESPONSE_MESSAGE']._serialized_end=310
  _globals['_CONNECTTOCHATREQUEST']._serialized_start=312
  _globals['_CONNECTTOCHATREQUEST']._serialized_end=334
  _globals['_CONNECTTOCHATRESPONSE']._serialized_start=336
  _globals['_CONNECTTOCHATRESPONSE']._serialized_end=376
  _globals['_SUBSCRIBETOGROUPCHATREQUEST']._serialized_start=378
  _globals['_SUBSCRIBETOGROUPCHATREQUEST']._serialized_end=407
  _globals['_SUBSCRIBETOGROUPCHATRESPONSE']._serialized_start=409
  _globals['_SUBSCRIBETOGROUPCHATRESPONSE']._serialized_end=456
  _globals['_CHATSERVER']._serialized_start=459
  _globals['_CHATSERVER']._serialized_end=809
# @@protoc_insertion_point(module_scope)
