from fastapi import FastAPI, Depends
from . import schemas, models
from .database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/blog")
def create_blog(request: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)  # adicionar novo blog
    db.commit()  # enviar as alterações
    db.refresh(new_blog)  # refresh no banco para refletir as alterações
    return new_blog  # retonar o blog recém criado


@app.get("/blog")
def get_all_blogs(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()  # query para retornar todos os blogs
    return blogs


@app.get("/blog/{id}")
def get_blog_by_id(id, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    return blog
