from sqlalchemy.orm import Session

from app import models, schemas
from auth import auth


def get_user_by_student_ticket(db: Session, user_student_ticket: int):
    return db.query(models.Users).filter(models.Users.student_ticket == user_student_ticket).first()


def get_user(db: Session, email: str):
    db_user = db.query(models.Users).filter(models.Users.email == email).first()
    print(db_user.email)
    print(db_user.password)
    user = schemas.User(email=db_user.email,
                        full_name=db_user.full_name,
                        student_ticket=db_user.student_ticket,
                        password=db_user.password)
    return user


def delete_user_by_student_ticket(db: Session, user_student_ticket: int):
    db_users = db.query(models.Users).filter(models.Users.student_ticket == user_student_ticket)
    db_user = db_users.first()
    db_users.delete()
    db.commit()
    return db_user


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Users).order_by(models.Users.student_ticket).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.Users(access_token=auth.create_access_token({"email": user.email, "password": user.password}),
                           student_ticket=user.student_ticket, password=user.password, full_name=user.full_name,
                           email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user(db: Session, user: schemas.UserCreate):
    db.query(models.Users).filter(models.Users.student_ticket == user.student_ticket) \
        .update({"password": user.password})
    db.commit()
    return db.query(models.Users).filter(models.Users.student_ticket == user.student_ticket).first()
