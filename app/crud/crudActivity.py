from sqlalchemy.orm import Session
from fastapi_auth0 import Auth0User
from app import models, schemas


def get_item_by_id(db: Session, item_id: int):
    return db.query(models.Activities).filter(models.Activities.id == item_id).first()


def delete_item_by_id(db: Session, item_id: int):
    db_items = db.query(models.Activities).filter(models.Activities.id == item_id)
    db_item = db_items.first()
    db_items.delete()
    db.commit()
    return db_item


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Activities).order_by(models.Activities.id).offset(skip).limit(limit).all()


def create_item(db: Session, activity: schemas.ActivitiesCreate, user_id: str):
    db_item = models.Activities(title=activity.title, work=activity.work, level=activity.level, date=activity.date,
                                responsible=activity.responsible, responsiblePosition=activity.responsiblePosition,
                                points=activity.points, status=activity.status,
                                user_id=user_id, id_request=activity.id_request)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def update_item(db: Session, activity: schemas.ActivitiesCreate, user_id: str):
    db.query(models.Activities).filter(models.Activities.id == activity.id) \
        .update({"title": activity.title, "work": activity.work, "level": activity.level, "date": activity.date,
                 "responsible": activity.responsible, "responsiblePosition": activity.responsiblePosition,
                 "points": activity.points, "status": activity.status,
                 "user_id": user_id, "request_id": activity.id_request})
    db.commit()
    return db.query(models.Activities).filter(models.Activities.id == activity.id).first()
