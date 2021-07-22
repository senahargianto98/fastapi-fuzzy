from typing import List, Optional
from pydantic import BaseModel

class TestBase(BaseModel):
    a1: int
    a2: int
    hasil: int

class FuzzyBase(BaseModel):
    query: str
    result: str

class Test(TestBase):
    class Config():
        orm_mode = True

class Fuzzy(FuzzyBase):
    class Config():
        orm_mode = True

class User(BaseModel):
    name:str
    email:str
    password:str

class ShowUser(BaseModel):
    name:str
    email:str
    class Config():
        orm_mode = True


class Login(BaseModel):
    username: str
    password:str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None

