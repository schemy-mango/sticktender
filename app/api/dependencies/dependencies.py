"""
This example includes the following dependencies:

get_db(): This is a dependency function that provides a SQLAlchemy session to other functions that need to interact with the database.

get_current_user(): This is a dependency function that validates the access token provided by the client and returns the associated user from the database. It raises an exception if the token is invalid or the user is not found.

get_current_active_user(): This is a dependency function that depends on get_current_user() and returns the current user only if they are active. If the user is not active, it raises an exception.

These dependencies are used in the create_plant() function in the previous example to ensure that only authenticated and active users can create new plant entries.
"""

#  Copyright (c) 2023. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.api.utils import security
from app.db import crud, models
from app.db.database import SessionLocal

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")


# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Dependency to get the current user based on the access token
async def get_current_user(
        db: Session = Depends(get_db),
        token: str = Depends(oauth2_scheme)
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    user = await security.get_user(token, db)
    if not user:
        raise credentials_exception
    return user


# Dependency to get the current active user
async def get_current_active_user(current_user: models.User = Depends(get_current_user)):
    if not crud.user.is_active(current_user):
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user
