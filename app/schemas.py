from typing import Optional, List
from datetime import date
from pydantic import BaseModel


class PrizesBase(BaseModel):
    id: Optional[int]
    title: str
    level: str
    degree: str
    place: int
    date: date
    points: float
    # user_id: str
    id_request: int


class PrizeCreate(PrizesBase):
    pass


class Prize(PrizesBase):
    user_id: str

    class Config:
        orm_mode = True


class ArtworksBase(BaseModel):
    id: Optional[int]
    title: str
    location: str
    date: date
    points: float
    # user_id: str
    id_request: int


class ArtworksCreate(ArtworksBase):
    pass


class Artwork(ArtworksBase):
    user_id: str

    class Config:
        orm_mode = True


class ActivitiesBase(BaseModel):
    id: Optional[int]
    title: str
    work: str
    level: str
    date: date
    responsible: str
    responsiblePosition: str
    points: float
    status: bool
    # user_id: str
    id_request: str


class ActivitiesCreate(ActivitiesBase):
    pass


class Activity(ActivitiesBase):
    user_id: str

    class Config:
        orm_mode = True
