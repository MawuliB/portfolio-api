from fastapi import APIRouter, HTTPException, Path, Depends
from config import sessionLocal
from sqlalchemy.orm import Session
from schemas import UserSchema, RequestUser, Response
import crud
from mail import send_specific_email

router = APIRouter()


def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/create")
async def create(request: RequestUser, db: Session = Depends(get_db)):
    # print(request.parameter)
    crud.create_user(db, user=request.parameter)
    return Response(code=200, status="OK", message="User Created").dict(
        exclude_none=True
    )


@router.get("/email")
async def get_emails(db: Session = Depends(get_db)):
    _user = crud.get_user(db, 0, 100)
    emails = []
    for e in _user:
        emails.append(e.email)
    return Response(
        code=200, status="OK", message="All Users Fetched", result=emails
    ).dict(exclude_none=True)


@router.get("/")
async def get(db: Session = Depends(get_db)):
    _user = crud.get_user(db, 0, 100)
    return Response(
        code=200, status="OK", message="All Users Fetched", result=_user
    ).dict(exclude_none=True)


@router.get("/{email}/{code}")
async def get_by_email(email: str, code: str, db: Session = Depends(get_db)):
    _user = crud.get_user_by_email(db, email=email)
    print(_user.code)
    if _user.code == code:
        return Response(
            code=200, status="OK", message="User Fetched", result=_user
        ).dict(exclude_none=True)
    else:
        return Response(code=400, status="error", message="Wrong Code").dict(
            exclude_none=True
        )

@router.get("/{username}")
async def get_by_username(username: str, db: Session = Depends(get_db)):
    _user = crud.get_user_by_username(db, username)
    user = {"name": _user.name, "email": _user.email, "socials": _user.socials, "data": _user.data}
    
    return Response(code=200, status="OK", message="User Fetched", result=user)

@router.post("/update")
async def update_user(request: RequestUser, db: Session = Depends(get_db)):
    _user = crud.update_user(
        db,
        name=request.parameter.name,
        email=request.parameter.email,
        username=request.parameter.username,
        socials=request.parameter.socials,
        data=request.parameter.data,
        code=request.parameter.code,
    )
    if _user == "error":
        return Response(code=400, status="error", message="Wrong Secret Code")

    return Response(code=200, status="OK", message="User Updated", result=_user)


@router.delete("/{email}")
async def delete(email: str, db: Session = Depends(get_db)):
    crud.remove_user(db, email)

    return Response(code=200, status="OK", message="User Deleted").dict(
        exclude_none=True
    )


@router.post('/send_email')
async def send_email(sender: str, receiver: str, title: str, body: str):
    send_specific_email(sender=sender, receiver=receiver, title=title, body=body)
    return Response(code=200, status="OK", message="Message Send")