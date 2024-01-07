from typing import List
from pydantic import BaseModel


class BlogBase(BaseModel):
    title: str
    body: str


class Blog(BlogBase):
    class Config:
        from_attributes = True


class User(BaseModel):
    name: str
    email: str
    password: str


# schema para retorno nas chamadas de criação no CRUD
# um parâmetro é adicionado ao main.py para confirmar esse schema no retorno da chamada
class UserResponse(BaseModel):
    name: str
    email: str
    blogs: List[Blog] = []

    class Config:
        from_attributes = True


# schema para retorno nas chamadas de criação no CRUD
# um parâmetro é adicionado ao main.py para confirmar esse schema no retorno da chamada
class BlogResponse(BaseModel):
    title: str
    body: str
    author: UserResponse

    class Config:
        from_attributes = True


class Login(BaseModel):
    username: str
    password: str
