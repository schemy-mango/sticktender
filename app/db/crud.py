from sqlalchemy.orm import Session

from app import schemas  # the Pydantic models / schemas
from . import models  # the SQLAlchemy models


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def create_user_plant(db: Session, plant: schemas.PlantCreate, user_id: int):
    db_plant = models.Plant(**plant.dict(), owner_id=user_id)
    db.add(db_plant)
    db.commit()
    db.refresh(db_plant)
    return db_plant


def create_user_site(db: Session, site: schemas.SiteCreate, user_id: int):
    db_site = models.Site(**site.dict(), owner_id=user_id)
    db.add(db_site)
    db.commit()
    db.refresh(db_site)
    return db_site
