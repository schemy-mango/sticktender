from pydantic import BaseModel

"""
To avoid confusion between the SQLAlchemy models and the Pydantic models,
we will have the file models.py with the SQLAlchemy models,
and the file schemas.py with the Pydantic models.
"""


class ItemBase(BaseModel):
    title: str
    description: str | None = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class PlantBase(BaseModel):
    title: str
    description: str | None = None


class PlantCreate(PlantBase):
    pass


class Plant(PlantBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class SiteBase(BaseModel):
    title: str
    description: str | None = None


class SiteCreate(SiteBase):
    pass


class Site(SiteBase):
    id: int
    owner_id: int
    plants: list[Plant] = []

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: list[Item] = []
    sites: list[Site] = []
    plants: list[Plant] = []

    # not sure if I need this field if I have plants linked to sites,
    # and sites linked to users. Maybe just add generic "unspecified" Site,
    # if a Plant isn't assigned to a Site?

    class Config:
        orm_mode = True
