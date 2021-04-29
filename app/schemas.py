from typing import Optional, List
from datetime import date
from pydantic import BaseModel


class PrizesBase(BaseModel):
    id: Optional[int]
    title: str
    level: int
    degree: int
    place: int
    date: date
    points: int
    # user_id: str
    id_request: str


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
    points: int
    # user_id: str
    id_request: str


class ArtworksCreate(ArtworksBase):
    pass


class Artwork(ArtworksBase):
    class Config:
        orm_mode = True


class ActivitiesBase(BaseModel):
    id: Optional[int]
    title: str
    work: str
    level: int
    date: date
    responsible: str
    responsiblePosition: str
    points: int
    status: bool
    # user_id: str
    id_request: str


class ActivitiesCreate(ActivitiesBase):
    pass


class Activity(ActivitiesBase):
    user_id: str

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None


class UserBase(BaseModel):
    email: str = None
    full_name: str = None
    student_ticket: str = None
    password: str = None
    disabled: Optional[bool] = None


class User(UserBase):
    class Config:
        orm_mode = True


class UserInDB(User):
    hashed_password: str


class UserCreate(User):
    pass
