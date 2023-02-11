from sqlalchemy.orm import Session
from model import User
from schemas import UserSchema
import random
from mail import send_mail

def get_user(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def create_user(db: Session, user: UserSchema):
    _user = User(
        name=user.name,
        email=user.email,
        username=user.username + str(int(random.random() * 10000)).zfill(4),
        socials=user.socials,
        data=user.data,
    )
    
    send_mail(_user.email, _user.username)
    db.add(_user)
    db.commit()
    db.refresh(_user)
    return _user


def remove_user(db: Session, email: str):
    _user = get_user_by_email(db, email)
    db.delete(_user)
    db.commit()


def update_user(
    db: Session, email: str, name: str, username: str, socials: dict, data: dict
):
    _user = get_user_by_email(db, email)

    _user.name, _user.email, _user.username, _user.socials, _user.data = (
        name,
        email,
        username,
        socials,
        data,
    )

    db.commit()
    db.refresh(_user)
    return _user
