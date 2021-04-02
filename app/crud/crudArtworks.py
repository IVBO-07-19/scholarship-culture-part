from sqlalchemy.orm import Session

from app import models, schemas


def get_item_by_id(db: Session, item_id: int):
    return db.query(models.Artworks).filter(models.Artworks.id == item_id).first()


def delete_item_by_id(db: Session, item_id: int):
    db_items = db.query(models.Artworks).filter(models.Artworks.id == item_id)
    db_item = db_items.first()
    db_items.delete()
    db.commit()
    return db_item


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Artworks).order_by(models.Artworks.id).offset(skip).limit(limit).all()


def create_item(db: Session, artwork: schemas.ArtworksCreate):
    db_item = models.Artworks(title=artwork.title, location=artwork.location,
                              date=artwork.date, points=artwork.points)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def update_item(db: Session, artwork: schemas.ArtworksCreate):
    db.query(models.Artworks).filter(models.Artworks.id == artwork.id) \
        .update({"title": artwork.title, "location": artwork.location,
                 "date": artwork.date, "points": artwork.points})
    db.commit()
    return db.query(models.Artworks).filter(models.Artworks.id == artwork.id).first()