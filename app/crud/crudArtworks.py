from sqlalchemy.orm import Session
from fastapi_auth0 import Auth0User
from app import models, schemas


def get_item_by_id(db: Session, item_id: int):
    return db.query(models.Artworks).filter(models.Artworks.id == item_id).first()


def get_item_by_id_request(db: Session, id_request: int):
    return db.query(models.Artworks).filter(models.Artworks.id_request == id_request).first()


def delete_item_by_id(db: Session, item_id: int):
    db_items = db.query(models.Artworks).filter(models.Artworks.id == item_id)
    db_item = db_items.first()
    db_items.delete()
    db.commit()
    return db_item


def get_items(db: Session, user_id: str, skip: int = 0, limit: int = 100):
    return db.query(models.Artworks).filter(models.Artworks.user_id == user_id).order_by(models.Artworks.id).offset(
        skip).limit(limit).all()


def create_item(db: Session, artwork: schemas.ArtworksCreate, user_id: str, id_request: int):
    db_item = models.Artworks(title=artwork.title, location=artwork.location,
                              date=artwork.date, points=artwork.points,
                              user_id=user_id, id_request=id_request)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def update_item(db: Session, artwork: schemas.ArtworksCreate, user_id: str, id_request: int):
    db.query(models.Artworks).filter(models.Artworks.id == artwork.id) \
        .update({"title": artwork.title, "location": artwork.location,
                 "date": artwork.date, "points": artwork.points, "user_id": user_id,
                 "id_request": id_request})
    db.commit()
    return db.query(models.Artworks).filter(models.Artworks.id == artwork.id).first()
