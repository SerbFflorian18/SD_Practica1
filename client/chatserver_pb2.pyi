from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ConnectToChatRequest(_message.Message):
    __slots__ = ("sender", "receiver")
    SENDER_FIELD_NUMBER: _ClassVar[int]
    RECEIVER_FIELD_NUMBER: _ClassVar[int]
    sender: str
    receiver: str
    def __init__(self, sender: _Optional[str] = ..., receiver: _Optional[str] = ...) -> None: ...

class ConnectToChatResponse(_message.Message):
    __slots__ = ("accept",)
    ACCEPT_FIELD_NUMBER: _ClassVar[int]
    accept: int
    def __init__(self, accept: _Optional[int] = ...) -> None: ...

class SendMessageRequest(_message.Message):
    __slots__ = ("sender", "receiver", "message")
    SENDER_FIELD_NUMBER: _ClassVar[int]
    RECEIVER_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    sender: str
    receiver: str
    message: str
    def __init__(self, sender: _Optional[str] = ..., receiver: _Optional[str] = ..., message: _Optional[str] = ...) -> None: ...

class SendMessageResponse(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class ReceiveMessageRequest(_message.Message):
    __slots__ = ("receiver",)
    RECEIVER_FIELD_NUMBER: _ClassVar[int]
    receiver: str
    def __init__(self, receiver: _Optional[str] = ...) -> None: ...

class ReceiveMessageResponse(_message.Message):
    __slots__ = ("messages",)
    class Message(_message.Message):
        __slots__ = ("sender", "message")
        SENDER_FIELD_NUMBER: _ClassVar[int]
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        sender: str
        message: str
        def __init__(self, sender: _Optional[str] = ..., message: _Optional[str] = ...) -> None: ...
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    messages: _containers.RepeatedCompositeFieldContainer[ReceiveMessageResponse.Message]
    def __init__(self, messages: _Optional[_Iterable[_Union[ReceiveMessageResponse.Message, _Mapping]]] = ...) -> None: ...

class SubscribeToGroupChatRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SubscribeToGroupChatResponse(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...
