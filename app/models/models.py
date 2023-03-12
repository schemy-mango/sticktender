#  Copyright (c) 2023. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.

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
