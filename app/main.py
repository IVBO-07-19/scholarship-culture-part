from typing import List

from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from app import models, schemas
from app.crud import crudPrizes, crudArtworks, crudActivity
from app.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# prizes for participation
@app.post("/api/culture/prizes/", response_model=schemas.Prize)
def create_item(item: schemas.PrizeCreate, db: Session = Depends(get_db)):
    return crudPrizes.create_item(db, item)


@app.get("/api/culture/prizes/", response_model=List[schemas.Prize])
def read_items(db: Session = Depends(get_db)):
    return crudPrizes.get_items(db)


@app.get("/api/culture/prizes/{item_id}", response_model=schemas.Prize)
def read_item(item_id: int, db: Session = Depends(get_db)):
    return crudPrizes.get_item_by_id(db, item_id=item_id)


@app.delete("/api/culture/prizes/{item_id}", response_model=schemas.Prize)
def delete_item(item_id: int, db: Session = Depends(get_db)):
    return crudPrizes.delete_item_by_id(db, item_id)


@app.put("/api/culture/prizes/", response_model=schemas.Prize)
def update_item(item: schemas.PrizeCreate, db: Session = Depends(get_db)):
    return crudPrizes.update_item(db, item)


# artworks
@app.post("/api/culture/artworks/", response_model=schemas.Artwork)
def create_item(item: schemas.ArtworksCreate, db: Session = Depends(get_db)):
    return crudArtworks.create_item(db, item)


@app.get("/api/culture/artworks/", response_model=List[schemas.Artwork])
def read_items(db: Session = Depends(get_db)):
    return crudArtworks.get_items(db)


@app.get("/api/culture/artworks/{item_id}", response_model=schemas.Artwork)
def read_item(item_id: int, db: Session = Depends(get_db)):
    return crudArtworks.get_item_by_id(db, item_id=item_id)


@app.delete("/api/culture/artworks/{item_id}", response_model=schemas.Artwork)
def delete_item(item_id: int, db: Session = Depends(get_db)):
    return crudArtworks.delete_item_by_id(db, item_id)


@app.put("/api/culture/artworks/", response_model=schemas.Artwork)
def update_item(item: schemas.ArtworksCreate, db: Session = Depends(get_db)):
    return crudArtworks.update_item(db, item)


# participation in university events or not
@app.post("/api/culture/activity/", response_model=schemas.Activity)
def create_item(item: schemas.ActivitiesCreate, db: Session = Depends(get_db)):
    return crudActivity.create_item(db, item)


@app.get("/api/culture/activity/", response_model=List[schemas.Activity])
def read_items(db: Session = Depends(get_db)):
    return crudActivity.get_items(db)


@app.get("/api/culture/activity/{item_id}", response_model=schemas.Activity)
def read_item(item_id: int, db: Session = Depends(get_db)):
    return crudActivity.get_item_by_id(db, item_id=item_id)


@app.delete("/api/culture/activity/{item_id}", response_model=schemas.Activity)
def delete_item(item_id: int, db: Session = Depends(get_db)):
    return crudActivity.delete_item_by_id(db, item_id)


@app.put("/api/culture/activity/", response_model=schemas.Activity)
def update_item(item: schemas.ActivitiesCreate, db: Session = Depends(get_db)):
    return crudActivity.update_item(db, item)
