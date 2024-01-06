from pydantic import BaseModel


class Blog(BaseModel):
    title: str
    body: str


# schema para retorno nas chamadas de criação no CRUD
# um parâmetro é adicionado ao main.py para confirmar esse schema no retorno da chamada
class BlogResponse(BaseModel):
    title: str
    body: str

    class Config:
        orm_mode = True


class User(BaseModel):
    name: str
    email: str
    password: str


# schema para retorno nas chamadas de criação no CRUD
# um parâmetro é adicionado ao main.py para confirmar esse schema no retorno da chamada
class UserResponse(BaseModel):
    name: str
    email: str

    class Config:
        orm_mode = True
