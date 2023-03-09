#  Copyright (c) 2023. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.

from datetime import date

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.dependencies import get_current_active_user
from app.api.dependencies import get_db
from app.api.models.plant import PlantCreate, Plant
from app.db import models as dbmodels

router = APIRouter()


@router.post("/plants", response_model=Plant)
async def create_plant(
        plant: PlantCreate,
        db: Session = Depends(get_db),
        current_user: dbmodels.User = Depends(get_current_active_user)
):
    new_plant = dbmodels.Plant(
        owner_id=current_user.id,
        created_at=date.today(),
        **plant.dict()
    )
    db.add(new_plant)
    db.commit()
    db.refresh(new_plant)
    return new_plant
