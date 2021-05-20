from typing import List

from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
from app import models, schemas
from app.crud import crudPrizes, crudArtworks, crudActivity
from app.database import SessionLocal, engine
from fastapi import FastAPI, Depends, Security, HTTPException
from fastapi_auth0 import Auth0, Auth0User
import os

auth0_domain = os.getenv('AUTH0_DOMAIN', 'suroegin503.eu.auth0.com')
auth0_api_audience = os.getenv('AUTH0_API_AUDIENCE', 'https://welcome/')

auth1 = Auth0(domain=auth0_domain, api_audience=auth0_api_audience, scopes={
    'Cultural': 'Part'
})

# client_id = zAmZ0t6DZtNFyTHM66UHptAjCzaV5p9Q, PdkS09Ig0EYVGK9KPYwncjKMGzXnAasI


models.Base.metadata.create_all(bind=engine)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI()

ACCESS_TOKEN_EXPIRE_MINUTES = 30


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# prizes for participation
@app.post("/api/culture/prizes/", response_model=schemas.Prize, dependencies=[Depends(auth1.implicit_scheme)])
def create_item(item: schemas.PrizeCreate, db: Session = Depends(get_db),
                user: Auth0User = Security(auth1.get_user)):
    if item.place > 0:
        return crudPrizes.create_item(db, item, user.id)
    else:
        raise HTTPException(status_code=406, detail={"Incorrect input"})


@app.get("/api/culture/prizes/", response_model=List[schemas.Prize], dependencies=[Depends(auth1.implicit_scheme)])
def read_items(db: Session = Depends(get_db),
               user: Auth0User = Security(auth1.get_user)):
    return crudPrizes.get_items(db)


@app.get("/api/culture/prizes/{item_id}", response_model=schemas.Prize, dependencies=[Depends(auth1.implicit_scheme)])
def read_item(item_id: int, db: Session = Depends(get_db),
              user: Auth0User = Security(auth1.get_user)):
    return crudPrizes.get_item_by_id(db, item_id=item_id)


@app.delete("/api/culture/prizes/{item_id}", response_model=schemas.Prize,
            dependencies=[Depends(auth1.implicit_scheme)])
def delete_item(item_id: int, db: Session = Depends(get_db),
                user: Auth0User = Security(auth1.get_user)):
    return crudPrizes.delete_item_by_id(db, item_id)


@app.put("/api/culture/prizes/", response_model=schemas.Prize, dependencies=[Depends(auth1.implicit_scheme)])
def update_item(item: schemas.PrizeCreate, db: Session = Depends(get_db),
                user: Auth0User = Security(auth1.get_user)):
    return crudPrizes.update_item(db, item, user.id)


# artworks
@app.post("/api/culture/artworks/", response_model=schemas.Artwork, dependencies=[Depends(auth1.implicit_scheme)])
def create_item(item: schemas.ArtworksCreate, db: Session = Depends(get_db),
                user: Auth0User = Security(auth1.get_user)):
    return crudArtworks.create_item(db, item, user.id)


@app.get("/api/culture/artworks/", response_model=List[schemas.Artwork], dependencies=[Depends(auth1.implicit_scheme)])
def read_items(db: Session = Depends(get_db),
               user: Auth0User = Security(auth1.get_user)):
    return crudArtworks.get_items(db)


@app.get("/api/culture/artworks/{item_id}", response_model=schemas.Artwork,
         dependencies=[Depends(auth1.implicit_scheme)])
def read_item(item_id: int, db: Session = Depends(get_db),
              user: Auth0User = Security(auth1.get_user)):
    return crudArtworks.get_item_by_id(db, item_id=item_id)


@app.delete("/api/culture/artworks/{item_id}", response_model=schemas.Artwork,
            dependencies=[Depends(auth1.implicit_scheme)])
def delete_item(item_id: int, db: Session = Depends(get_db),
                user: Auth0User = Security(auth1.get_user)):
    return crudArtworks.delete_item_by_id(db, item_id)


@app.put("/api/culture/artworks/", response_model=schemas.Artwork, dependencies=[Depends(auth1.implicit_scheme)])
def update_item(item: schemas.ArtworksCreate, db: Session = Depends(get_db),
                user: Auth0User = Security(auth1.get_user)):
    return crudArtworks.update_item(db, item, user.id)


# participation in university events or not
@app.post("/api/culture/activity/", response_model=schemas.Activity, dependencies=[Depends(auth1.implicit_scheme)])
def create_item(item: schemas.ActivitiesCreate, db: Session = Depends(get_db),
                user: Auth0User = Security(auth1.get_user)):
    return crudActivity.create_item(db, item, user.id)


@app.get("/api/culture/activity/", response_model=List[schemas.Activity], dependencies=[Depends(auth1.implicit_scheme)])
def read_items(db: Session = Depends(get_db),
               user: Auth0User = Security(auth1.get_user)):
    return crudActivity.get_items(db)


@app.get("/api/culture/activity/{item_id}", response_model=schemas.Activity,
         dependencies=[Depends(auth1.implicit_scheme)])
def read_item(item_id: int, db: Session = Depends(get_db),
              user: Auth0User = Security(auth1.get_user)):
    return crudActivity.get_item_by_id(db, item_id=item_id)


@app.delete("/api/culture/activity/{item_id}", response_model=schemas.Activity,
            dependencies=[Depends(auth1.implicit_scheme)])
def delete_item(item_id: int, db: Session = Depends(get_db),
                user: Auth0User = Security(auth1.get_user)):
    return crudActivity.delete_item_by_id(db, item_id)


@app.put("/api/culture/activity/", response_model=schemas.Activity, dependencies=[Depends(auth1.implicit_scheme)])
def update_item(item: schemas.ActivitiesCreate, db: Session = Depends(get_db),
                user: Auth0User = Security(auth1.get_user)):
    return crudActivity.update_item(db, item, user.id)
