import fastapi
from pydantic import BaseModel, Field
from typing import Optional, List

router = fastapi.APIRouter()

class User(BaseModel):
    email: str # required
    is_active: bool # required
    bio: Optional[str] = Field(None) # optional field

users = []


@router.get("/users", response_model=List[User]) # response should be a list of dictionery of type User
async def get_users():
    return users

@router.post("/users")
async def create_user(user: User):
    users.routerend(user)
    return "User created"

@router.get("/users/{user_id}")
async def get_user(user_id: int): 
    return {'user': users[user_id]}