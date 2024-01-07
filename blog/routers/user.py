from fastapi import APIRouter, Depends
from .. import schemas, database
from sqlalchemy.orm import Session
from ..repository import user_r

router = APIRouter(
    prefix="/user",  # configuração para definir parte da rota padrão
    tags=["Users"],  # configuração para definir a tag na documentação
)

get_db = database.get_db


@router.post("/", response_model=schemas.UserResponse)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user_r.create(db, request)


@router.get("/{id}", response_model=schemas.UserResponse)
def get_user_by_id(id: int, db: Session = Depends(get_db)):
    return user_r.get_by_id(db, id)
