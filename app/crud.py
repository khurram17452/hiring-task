from sqlalchemy.orm import Session
from . import models, schemas
from fastapi import HTTPException

def create_user(db: Session, user: schemas.UserCreate):
    # Check if email already exists
    existing_user = db.query(models.User).filter(models.User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    db_user = models.User(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.User).offset(skip).limit(limit).all()

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def delete_user(db: Session, user_id: int):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
    return user

def update_user(db: Session, user_id: int, updated_data: schemas.UserCreate):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        return None

    # Prevent duplicate emails
    existing_user = db.query(models.User).filter(
        models.User.email == updated_data.email, models.User.id != user_id
    ).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already in use")

    user.name = updated_data.name
    user.email = updated_data.email
    db.commit()
    db.refresh(user)
    return user