from typing import Optional
from pydantic import BaseModel


class ItemBase(BaseModel):
    id: Optional[int]
    fieldA: str
    fieldB: str


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    class Config:
        orm_mode = True
