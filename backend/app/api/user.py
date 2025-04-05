# API router
from fastapi import APIRouter, HTTPException
from typing import List
from pydantic import BaseModel
from app.models.user import User
from app.schema.user import UserCreate, UserRead

router = APIRouter()

fake_users_db = []

@router.post("/users/", response_model=UserRead)
def create_user(user: UserCreate):
    new_user = User(**user.dict())
    fake_users_db.append(new_user)
    return new_user

@router.get("/users/", response_model=List[UserRead])
def read_users():
    return fake_users_db

@router.get("/users/{user_id}", response_model=UserRead)
def read_user(user_id: int):
    for user in fake_users_db:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")