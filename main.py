from fastapi import FastAPI, Path, Query
from pydantic import BaseModel, Field
from typing import Optional, List

app = FastAPI(
    title="Fast API LMS",
    description="API for managing students and courses in a LMS",
    version="0.1.0",
    contact={
        "name": "Srikar",
        "email": "srikar@example.com",
    },
    license_info={
        "name": "MIT License",
        "url": "https://opensource.org/licenses/MIT",
    },
)

class User(BaseModel):
    email: str # required
    is_active: bool # required
    bio: Optional[str] = Field(None) # optional field

users = []

@app.get("/users", response_model=List[User]) # response should be a list of dictionery of type User
async def get_users():
    return users

@app.post("/users")
async def create_user(user: User):
    users.append(user)
    return "User created"

@app.get("/users/{user_id}")
async def get_user(
    user_id: int = Path(..., description="The ID of the user", gt=0, lt=3), # user_id is a path parameter - it will be displayed in the URL, gt -> greater than, lt -> less than
    q: str = Query(None, max_length=50), # query -> is a paramater after ? in the URL for filtering, path -> is a path parameter in the URL
    ): 
    return {'user': users[user_id], 'q': q}