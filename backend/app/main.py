#  Copyright (c) 2023. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.

from fastapi import FastAPI
from fastapi_users import FastAPIUsers
from fastapi_users.db import SQLAlchemyUserDatabase
from pydantic import EmailStr
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import declarative_base

DATABASE_URL = "postgresql://user:password@localhost/plantcare"
SECRET = "SECRET_KEY"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

engine = create_async_engine(DATABASE_URL, echo=True, future=True)
Base = declarative_base()

app = FastAPI()

from models import UserDB, UserCreate, User, UserUpdate

user_db = SQLAlchemyUserDatabase(UserDB, database=engine)

fastapi_users = FastAPIUsers(
    user_db,
    [user_db],
    User,
    UserCreate,
    UserUpdate,
    UserDB,
    SECRET,
    ALGORITHM,
    ACCESS_TOKEN_EXPIRE_MINUTES,
)


@app.post("/register")
async def register_user(email: EmailStr, password: str):
    user = await fastapi_users.create_user(UserCreate(email=email, password=password))
    return user


from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi_users import FastAPIUsers
from fastapi_users.db import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import declarative_base

DATABASE_URL = "postgresql://user:password@localhost/plantcare"
SECRET = "SECRET_KEY"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

engine = create_async_engine(DATABASE_URL, echo=True, future=True)
Base = declarative_base()

app = FastAPI()

from models import UserDB, UserCreate, User, UserUpdate

user_db = SQLAlchemyUserDatabase(UserDB, database=engine)

fastapi_users = FastAPIUsers(
    user_db,
    [user_db],
    User,
    UserCreate,
    UserUpdate,
    UserDB,
    SECRET,
    ALGORITHM,
    ACCESS_TOKEN_EXPIRE_MINUTES,
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await fastapi_users.authenticate(email=form_data.username, password=form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    access_token = fastapi_users.create_access_token(user.id)
    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/protected")
async def protected_route(token: str = Depends(oauth2_scheme)):
    user = await fastapi_users.get_current_active_user(token)
    return {"message": "You are authenticated", "user": user}
