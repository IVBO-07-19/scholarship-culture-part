from typing import List

from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from app import models, schemas
from app.crud import crudPrizes, crudArtworks, crudActivity
from app.database import SessionLocal, engine
from auth import auth
from datetime import timedelta
from fastapi import FastAPI, Depends, Security
from fastapi_auth0 import Auth0, Auth0User
import os

auth0_domain = os.getenv('AUTH0_DOMAIN', 'dev-ntt3e8ta.us.auth0.com')
auth0_api_audience = os.getenv('AUTH0_API_AUDIENCE', 'culture')

auth1 = Auth0(domain=auth0_domain, api_audience=auth0_api_audience, scopes={
    'read:blabla': 'Read BlaBla resource'
})

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


# @app.post("/token", response_model=schemas.Token)
# async def login_for_access_token(db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):
#     user = auth.authenticate_user(db, form_data.username, form_data.password)
#     if not user:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Incorrect username or password",
#             headers={"WWW-Authenticate": "Bearer"},
#         )
#     access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
#     access_token = auth.create_access_token(
#         data={"sub": user.email}, expires_delta=access_token_expires
#     )
#     return {"access_token": access_token, "token_type": "bearer"}


# @app.get("/api/culture/users/me/", response_model=schemas.UserBase, dependencies=[Depends(auth1.implicit_scheme)])
# async def read_users_me(current_user: schemas.User = Depends(auth.get_current_active_user)):
#     return current_user
#
#
# @app.get("/api/culture/users/me/items/")
# async def read_own_items(current_user: schemas.User = Depends(auth1.implicit_scheme)):
#     return [{"user_student_ticket": current_user.student_ticket, "email": current_user.email}]


# prizes for participation
@app.post("/api/culture/prizes/", response_model=schemas.Prize, dependencies=[Depends(auth1.implicit_scheme)])
def create_item(item: schemas.PrizeCreate, db: Session = Depends(get_db)):
    return crudPrizes.create_item(db, item)


@app.get("/api/culture/prizes/", response_model=List[schemas.Prize], dependencies=[Depends(auth1.implicit_scheme)])
def read_items(db: Session = Depends(get_db)):
    return crudPrizes.get_items(db)


@app.get("/api/culture/prizes/{item_id}", response_model=schemas.Prize, dependencies=[Depends(auth1.implicit_scheme)])
def read_item(item_id: int, db: Session = Depends(get_db)):
    return crudPrizes.get_item_by_id(db, item_id=item_id)


@app.delete("/api/culture/prizes/{item_id}", response_model=schemas.Prize, dependencies=[Depends(auth1.implicit_scheme)])
def delete_item(item_id: int, db: Session = Depends(get_db)):
    return crudPrizes.delete_item_by_id(db, item_id)


@app.put("/api/culture/prizes/", response_model=schemas.Prize, dependencies=[Depends(auth1.implicit_scheme)])
def update_item(item: schemas.PrizeCreate, db: Session = Depends(get_db)):
    return crudPrizes.update_item(db, item)


# artworks
@app.post("/api/culture/artworks/", response_model=schemas.Artwork, dependencies=[Depends(auth1.implicit_scheme)])
def create_item(item: schemas.ArtworksCreate, db: Session = Depends(get_db)):
    return crudArtworks.create_item(db, item)


@app.get("/api/culture/artworks/", response_model=List[schemas.Artwork], dependencies=[Depends(auth1.implicit_scheme)])
def read_items(db: Session = Depends(get_db)):
    return crudArtworks.get_items(db)


@app.get("/api/culture/artworks/{item_id}", response_model=schemas.Artwork, dependencies=[Depends(auth1.implicit_scheme)])
def read_item(item_id: int, db: Session = Depends(get_db)):
    return crudArtworks.get_item_by_id(db, item_id=item_id)


@app.delete("/api/culture/artworks/{item_id}", response_model=schemas.Artwork, dependencies=[Depends(auth1.implicit_scheme)])
def delete_item(item_id: int, db: Session = Depends(get_db)):
    return crudArtworks.delete_item_by_id(db, item_id)


@app.put("/api/culture/artworks/", response_model=schemas.Artwork, dependencies=[Depends(auth1.implicit_scheme)])
def update_item(item: schemas.ArtworksCreate, db: Session = Depends(get_db)):
    return crudArtworks.update_item(db, item)


# participation in university events or not
@app.post("/api/culture/activity/", response_model=schemas.Activity, dependencies=[Depends(auth1.implicit_scheme)])
def create_item(item: schemas.ActivitiesCreate, db: Session = Depends(get_db)):
    return crudActivity.create_item(db, item)


@app.get("/api/culture/activity/", response_model=List[schemas.Activity], dependencies=[Depends(auth1.implicit_scheme)])
def read_items(db: Session = Depends(get_db)):
    return crudActivity.get_items(db)


@app.get("/api/culture/activity/{item_id}", response_model=schemas.Activity, dependencies=[Depends(auth1.implicit_scheme)])
def read_item(item_id: int, db: Session = Depends(get_db)):
    return crudActivity.get_item_by_id(db, item_id=item_id)


@app.delete("/api/culture/activity/{item_id}", response_model=schemas.Activity, dependencies=[Depends(auth1.implicit_scheme)])
def delete_item(item_id: int, db: Session = Depends(get_db)):
    return crudActivity.delete_item_by_id(db, item_id)


@app.put("/api/culture/activity/", response_model=schemas.Activity, dependencies=[Depends(auth1.implicit_scheme)])
def update_item(item: schemas.ActivitiesCreate, db: Session = Depends(get_db)):
    return crudActivity.update_item(db, item)
