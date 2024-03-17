import uuid

from sqlalchemy.orm import Session

import crud.user
from dependencies import get_db
from fastapi import APIRouter, Depends, HTTPException, Request, Response, status
from schemas import UserSchema

router = APIRouter(tags=["auth"])


@router.post("/login", response_model=UserSchema.User)
async def login(response: Response, email: str, password: str, db: Session = Depends(get_db)):
    db_user = crud.user.get_user_by_email_and_password(db, email=email, password=password)
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="メールアドレスまたはパスワードが正しくありません。"
        )
    session_id = uuid.uuid4()
    db_user = crud.user.set_session_id(db, user_id=db_user.id, session_id=session_id)
    response.set_cookie(key="session_id", value=session_id)
    return db_user


@router.post("/logout")
async def logout(request: Request, response: Response, db: Session = Depends(get_db)):
    session_id = request.cookies.get("session_id")
    db_user = crud.user.drop_session_id(db, session_id=session_id)
    response.delete_cookie(key="session_id")
    return db_user
