from sqlalchemy.orm import Session

from app import models, schemas


def get_item_by_id(db: Session, item_id: int):
    return db.query(models.Items).filter(models.Items.id == item_id).first()


def delete_item_by_id(db: Session, item_id: int):
    db_items = db.query(models.Items).filter(models.Items.id == item_id)
    db_item = db_items.first()
    db_items.delete()
    db.commit()
    return db_item


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Items).order_by(models.Items.id).offset(skip).limit(limit).all()


def create_item(db: Session, item: schemas.ItemCreate):
    db_item = models.Items(fieldA=item.fieldA, fieldB=item.fieldB)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def update_item(db: Session, item: schemas.ItemCreate):
    db.query(models.Items).filter(models.Items.id == item.id)\
        .update({"fieldA": item.fieldA, "fieldB": item.fieldB})
    db.commit()
    return db.query(models.Items).filter(models.Items.id == item.id).first()