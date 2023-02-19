from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LoginRequest(_message.Message):
    __slots__ = ["password", "username"]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    password: str
    username: str
    def __init__(self, username: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class LoginResponse(_message.Message):
    __slots__ = ["access_token", "refresh_token"]
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    access_token: str
    refresh_token: str
    def __init__(self, access_token: _Optional[str] = ..., refresh_token: _Optional[str] = ...) -> None: ...

class User(_message.Message):
    __slots__ = ["firstname", "id", "is_active", "lastname", "role", "username"]
    FIRSTNAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    IS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    LASTNAME_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    firstname: str
    id: str
    is_active: bool
    lastname: str
    role: str
    username: str
    def __init__(self, id: _Optional[str] = ..., firstname: _Optional[str] = ..., lastname: _Optional[str] = ..., role: _Optional[str] = ..., is_active: bool = ..., username: _Optional[str] = ...) -> None: ...

class UserListRequest(_message.Message):
    __slots__ = ["page", "page_size"]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    page: int
    page_size: int
    def __init__(self, page: _Optional[int] = ..., page_size: _Optional[int] = ...) -> None: ...

class UserListResponse(_message.Message):
    __slots__ = ["count", "next", "previous", "results"]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    NEXT_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_FIELD_NUMBER: _ClassVar[int]
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    count: int
    next: str
    previous: str
    results: _containers.RepeatedCompositeFieldContainer[User]
    def __init__(self, count: _Optional[int] = ..., next: _Optional[str] = ..., previous: _Optional[str] = ..., results: _Optional[_Iterable[_Union[User, _Mapping]]] = ...) -> None: ...

class UserRetrieveRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...
