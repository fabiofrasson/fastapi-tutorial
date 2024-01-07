from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from .. import schemas, models, database
from sqlalchemy.orm import Session
from ..repository import blog_r

router = APIRouter(
    prefix="/blog",  # configuração para definir parte da rota padrão
    tags=["Blogs"],  # configuração para definir a tag na documentação
)

get_db = database.get_db


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_blog(request: schemas.Blog, db: Session = Depends(get_db)):
    return blog_r.create(db, request)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id: int, db: Session = Depends(get_db)):
    return blog_r.delete(db, id)


@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_blog(id: int, request: schemas.Blog, db: Session = Depends(get_db)):
    return blog_r.update(db, id, request)


@router.get("/", response_model=List[schemas.BlogResponse])
def get_all_blogs(db: Session = Depends(get_db)):
    return blog_r.get_all(db)


@router.get(
    "/{id}", status_code=status.HTTP_200_OK, response_model=schemas.BlogResponse
)
def get_blog_by_id(id: int, db: Session = Depends(get_db)):
    return blog_r.get_by_id(db, id)
