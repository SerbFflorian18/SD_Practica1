from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Insult(_message.Message):
    __slots__ = ("insult", "severity")
    INSULT_FIELD_NUMBER: _ClassVar[int]
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    insult: str
    severity: float
    def __init__(self, insult: _Optional[str] = ..., severity: _Optional[float] = ...) -> None: ...

class Insults(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, value: _Optional[_Iterable[str]] = ...) -> None: ...

class InsultName(_message.Message):
    __slots__ = ("insult_name",)
    INSULT_NAME_FIELD_NUMBER: _ClassVar[int]
    insult_name: str
    def __init__(self, insult_name: _Optional[str] = ...) -> None: ...

class Severity(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: float
    def __init__(self, value: _Optional[float] = ...) -> None: ...
