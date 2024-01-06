from fastapi import FastAPI
from . import models
from .database import engine
from .routers import blog, user

tags_metadata = [
    {
        "name": "Users",
        "description": "Operations with users.",
    },
    {"name": "Blogs", "description": "Manage blogs."},
]

app = FastAPI()
app.include_router(blog.router)
app.include_router(user.router)

# models.Base.metadata.drop_all(engine)
models.Base.metadata.create_all(bind=engine)
