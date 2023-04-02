from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

"""
To avoid confusion between the SQLAlchemy models and the Pydantic models, 
we will have the file models.py with the SQLAlchemy models, 
and the file schemas.py with the Pydantic models.
"""


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")


class Site(Base):
    __tablename__ = "sites"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    sun_exposure_id = Column(Integer, ForeignKey("need_sun.id"))
    temperature = Column(Integer)
    humidity_id = Column(Integer, ForeignKey("need_sun.id"))
    outdoors = Column(Boolean, default=False)
    owner_id = Column(Integer, ForeignKey("users.id"))

    site = relationship("Plant", back_populates="site")


class Plant(Base):
    __tablename__ = "plants"

    id = Column(Integer, primary_key=True, index=True)
    name_common = Column(String, index=True)
    name_scientific = Column(String, index=True)
    description = Column(String, index=True)
    need_sun_id = Column(Integer, ForeignKey("need_sun.id"))
    need_sun_comment = Column(String, index=True)
    site_id = Column(Integer, ForeignKey("sites.id"))
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="plants")


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")
