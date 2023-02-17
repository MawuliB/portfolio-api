from sqlalchemy.orm import Session
from model import User
from schemas import UserSchema
import random
from mail import send_mail
import string
import secrets


def get_user(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()


def create_user(db: Session, user: UserSchema):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = "".join(secrets.choice(alphabet) for i in range(16))
    _user = User(
        name=user.name,
        email=user.email,
        username=user.username + str(int(random.random() * 10000)).zfill(4),
        socials=user.socials,
        data=user.data,
        code=password,
    )

    send_mail(
        _user.email, _user.username, _user.code, "Your Site is ready for viewing at"
    )
    db.add(_user)
    db.commit()
    db.refresh(_user)
    return _user


def remove_user(db: Session, email: str):
    _user = get_user_by_email(db, email)
    db.delete(_user)
    db.commit()


def update_user(
    db: Session, email: str, name: str, username: str, socials: dict, data: dict, code
):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = "".join(secrets.choice(alphabet) for i in range(16))
    _user = get_user_by_email(db, email)
    if _user.code == code:
        (
            _user.name,
            _user.email,
            _user.username,
            _user.socials,
            _user.data,
            _user.code,
        ) = (
            name,
            email,
            username,
            socials,
            data,
            password,
        )

        db.commit()
        send_mail(
            _user.email, _user.username, _user.code, "Your Site has been updated at"
        )
        db.refresh(_user)
        return _user
    else:
        return "error"
