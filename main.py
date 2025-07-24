from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from uuid import uuid4

app = FastAPI()

# In-memory database
users_db = []

# Base user model
class User(BaseModel):
    name: str
    email: str
    password: str

# Stored user with ID
class StoredUser(User):
    id: str

# Register a new user
@app.post("/register")
def register_user(user: User):
    # Check if user already exists
    for existing_user in users_db:
        if existing_user.email == user.email:
            raise HTTPException(status_code=400, detail="Email already registered")
    
    new_user = StoredUser(id=str(uuid4()), **user.dict())
    users_db.append(new_user)
    return {"message": "User registered successfully", "user_id": new_user.id}

# Login user
class LoginRequest(BaseModel):
    email: str
    password: str

@app.post("/login")
def login_user(credentials: LoginRequest):
    for user in users_db:
        if user.email == credentials.email and user.password == credentials.password:
            return {"token": f"fake-jwt-token-for-{user.id}"}
    raise HTTPException(status_code=401, detail="Invalid email or password")

# Get all users
@app.get("/user", response_model=List[StoredUser])
def get_all_users():
    return users_db

# Delete a user by ID
@app.delete("/user/{id}")
def delete_user(id: str):
    for i, user in enumerate(users_db):
        if user.id == id:
            del users_db[i]
            return {"message": "User deleted successfully"}
    raise HTTPException(status_code=404, detail="User not found")
