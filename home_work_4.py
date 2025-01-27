from fastapi import FastAPI, Path, HTTPException
from pydantic import BaseModel


app = FastAPI() # Start - uvicorn home_work_4:app
users = []

class User(BaseModel):
    id: int
    username: str
    age: int


@app.get('/users')
async def get_users() -> list:
    return users


@app.post('/users/{username}/{age}')
async def add_users(username: str =
                    Path(min_length=5, max_length=20, description="Enter your name", example="Mihail")
                        , age: int =
                    Path(ge=18, le=120, description='Enter age',example=24)) -> User:
    user = User(id=len(users)+1, username=username, age=age)
    users.append(user)
    return user


@app.put('/user/{user_id}/{username}/{age}')
async def put_users(user_id: int =
                    Path(ge=1, le=100, description='Enter User ID', example=1)
                , username: str =
                    Path(min_length=5, max_length=20, description='Enter username',example='UrbanUser')
                      , age: int =
                    Path(ge=18, le=120, description='Enter age',example=24)) -> User:

        for user in users:
            if user.id == user_id:
                user.username = username
                user.age = age
                return user
        raise HTTPException(status_code=404, detail="User was not found")




@app.delete('/user/{user_id}')
async def del_users(user_id: int = Path(ge=1, le=100, description='Enter User ID', example=1)) -> User:
    for user in users:
        if user.id == user_id:
            return users.pop(users.index(user))
    raise HTTPException(status_code=404, detail="User was not found")
