#  Copyright (c) 2023. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.

from datetime import date
from typing import Optional

from pydantic import BaseModel


class PlantBase(BaseModel):
    name: str
    description: Optional[str] = None
    species: Optional[str] = None
    variety: Optional[str] = None
    plant_type: Optional[str] = None
    location: Optional[str] = None


class PlantCreate(PlantBase):
    pass


class Plant(PlantBase):
    id: int
    owner_id: int
    created_at: date

    class Config:
        orm_mode = True
