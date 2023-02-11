from typing import List, Optional, Generic, TypeVar, Dict
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel

T = TypeVar("T")


class UserSchema(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    username: Optional[str] = None
    socials: Optional[Dict] = None
    data: Optional[Dict] = None

    class config:
        orm_mode = True


class Request(GenericModel, Generic[T]):
    parameter: Optional[T] = Field(...)


class RequestUser(BaseModel):
    parameter: UserSchema = Field(...)


class Response(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]
