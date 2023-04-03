from pydantic import BaseModel


class SiteBase(BaseModel):
    name: str
    description: str | None = None


class SiteCreate(SiteBase):
    pass


class Site(SiteBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class PlantBase(BaseModel):
    name_common: str
    description: str | None = None


class PlantCreate(PlantBase):
    pass


class Plant(PlantBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


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


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: list[Item] = []

    class Config:
        orm_mode = True