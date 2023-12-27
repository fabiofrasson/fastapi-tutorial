from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return {"data": "blog list"}


@app.get("/blog/unpublished")
def show_unpublished():
    # fetch unpublished blog posts
    return {"data": "all unpublished blog posts"}


@app.get("/blog/{id}")
def show_blog_post(id: int):
    # fetch blog with id = id
    return {"data": id}


@app.get("/blog/{id}/comments")
def show_comments(id: int):
    # fetch comments of blog post with id = id
    # anteriormente estava 
    # return {"data": "here are the comments for blog post [" + id + "]"} 
    # e enviar a requisição retornava 
    # internal server error
    return {"data": ["1", "2"]}
