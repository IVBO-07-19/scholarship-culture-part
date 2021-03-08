from random import randint
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder

app = FastAPI()
data = []
last_id = 0


def random():
    result = ""
    for i in range(randint(5, 15)):
        r = randint(0, 61)
        if r < 10:
            result += chr(r + 48)
        elif r < 36:
            result += chr(r + 55)
        else:
            result += chr(r + 61)
    return result


class Item(BaseModel):
    id: Optional[int]
    fieldA: Optional[str]
    fieldB: Optional[str]


def init(item_id, field_a, field_b):
    item = Item()
    item.id = item_id
    item.fieldA = field_a
    item.fieldB = field_b
    return item


def generate():
    global last_id, data
    data = []
    for i in range(1, 11):
        data.append(init(i, random(), random()))
        last_id = i


generate()


@app.get("/api/cultural-part/example")
async def root():
    return data


@app.get("/api/cultural-part/example/{item_id}")
async def find_by_id(item_id: int):
    for i in range(len(data)):
        if data.__getitem__(i).id == item_id:
            return data.__getitem__(i)
    return {}


@app.post("/api/cultural-part/example")
async def respond(item: Item):
    global last_id
    last_id += 1
    item.id = last_id
    data.append(item)
    return item


@app.get("/api/cultural-part/clean")
async def clean():
    generate()
    return {}
