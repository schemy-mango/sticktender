#  Copyright (c) 2023. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.

from typing import Union

import uvicorn
from PIL import Image
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    name_binominal: str
    is_alive: Union[bool, None] = None
    misting: Union[int, None] = None


@app.get("/")
def read_root():
    return {"message": "Ready."}


@app.get("/plants/{plant_id}")
def get_plant(plant_id: int):
    return {"plant_id": plant_id}


def main():
    im = Image.open("1219391.jpg")
    print(im.format, im.size, im.mode)
    im.show()


if __name__ == '__main__':
    uvicorn.run("app.main:app", port=5000, reload=True, access_log=False)
