#  Copyright (c) 2023. Marek Krysiak

from typing import Union

from pydantic import BaseModel


class PlantModel(BaseModel):
    name: str
    name_binominal: str
    is_alive: Union[bool, None] = None
    misting: Union[int, None] = None


class SiteModel(BaseModel):
    name: str
    sun_exposure: int
    humidity: int
    temperature: int
