#  Copyright (c) 2023. Marek Krysiak

import uvicorn
from PIL import Image
from fastapi import FastAPI

from app.models import PlantModel, SiteModel

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Ready."}


@app.get("/plants/{plant_id}")
def get_plant(plant_id: int):
    return {"plant_id": plant_id}


@app.get("/sites/{site_id}")
def get_site(site_id: int):
    return {"site_id": site_id}


@app.post("/add_plant")
def add_plant(plant_details: PlantModel):
    return {"message": "Done"}


@app.post("/add_site")
def add_site(site_details: SiteModel):
    return {"message": "Done"}


def main():
    im = Image.open("1219391.jpg")
    print(im.format, im.size, im.mode)
    im.show()


if __name__ == '__main__':
    uvicorn.run("app.main:app", port=5000, reload=True, access_log=False)
