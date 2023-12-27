import uvicorn
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


@app.get("/blog")
# necessário fazer validação do booleano, caso contrário será lido como string
def index(limit=10, published: bool = True, sort: Optional[str] = None):
    # definir valor padrão para QP, delimitar o tipo e colocá-lo como opcional

    # only get 10 published blog posts
    if published:
        return {"data": f"{limit} published blogs from the db"}
    else:
        return {"data": f"{limit} blogs from the db"}


@app.get("/blog/unpublished")
def show_unpublished():
    # fetch unpublished blog posts
    return {"data": "all unpublished blog posts"}


@app.get("/blog/{id}")
def show_blog_post(id: int):
    # fetch blog with id = id
    return {"data": id}


@app.get("/blog/{id}/comments")
def show_comments(id: int, limit=10):
    # fetch comments of blog post with id = id
    # anteriormente estava
    # return {"data": "here are the comments for blog post [" + id + "]"}
    # e enviar a requisição retornava
    # internal server error
    return {"data": ["1", "2"]}


# definição de model
class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


@app.post("/blog")
# delimitação do parâmetro e tipo desse parâmetro
def create_blog_post(blog: Blog):
    # string formatada, utilizando os valores enviados na requisição
    return {"data": f"Blog post was created with title: {blog.title}"}