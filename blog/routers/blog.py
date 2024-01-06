from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from .. import schemas, models, database
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/blog", # configuração para definir parte da rota padrão
    tags=["Blogs"] # configuração para definir a tag na documentação
)

get_db = database.get_db


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_blog(request: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)  # adicionar novo blog
    db.commit()  # enviar as alterações
    db.refresh(new_blog)  # refresh no banco para refletir as alterações
    return new_blog  # retonar o blog recém criado


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found"
        )
    blog.delete(synchronize_session=False)
    db.commit()
    return {"message": f"Blog with id {id} was deleted"}


@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_blog(id, request: schemas.Blog, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found"
        )
    blog.update(request.dict())
    db.commit()
    return {"message": f"Blog with id {id} was updated"}


@router.get("/", response_model=List[schemas.BlogResponse])
def get_all_blogs(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()  # query para retornar todos os blogs
    return blogs


@router.get(
    "/{id}", status_code=status.HTTP_200_OK, response_model=schemas.BlogResponse
)
def get_blog_by_id(id, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        # forma mais extensa de declarar um retorno e código em casos de de erro
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"detail": f"Blog with id {id} is not available"}
        # forma mais concisa
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with id {id} is not available",
        )
    return blog
