import fastapi
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Optional, List
from pydantic_schemas.user import UserCreate, User
from API.utils.users import get_user, get_user_by_email, get_users, create_user
from DB.db_setup import get_db

router = fastapi.APIRouter()

@router.get("/users", response_model=List[User]) # response should be a list of dictionery of type User
async def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = get_users(db, skip=skip, limit=limit)
    return users

@router.post("/users")
async def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db=db, user=user)

@router.get("/users/{user_id}")
async def read_user(user_id: int, db: Session = Depends(get_db)): 
    return get_user(db=db, user_id=user_id)