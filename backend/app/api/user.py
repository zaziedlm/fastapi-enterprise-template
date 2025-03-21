from fastapi import APIRouter, Depends
from app.usecases.user import UserService
from app.db import get_db

router = APIRouter()

@router.get("/users/{user_id}")
def read_user(user_id: int, db=Depends(get_db)):
    service = UserService(db)
    return service.get_user(user_id)
