from sqlalchemy.orm import Session

import crud.user
from database.database import get_db_session
from fastapi import Depends, HTTPException, Request, status


def get_db():
    SessionLocal = get_db_session()
    db = SessionLocal()
    try:
        yield db
        db.commit()
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()


def get_current_user(request: Request, db: Session = Depends(get_db)):
    session_id = request.cookies.get("session_id")
    db_user = crud.user.get_user_by_session_id(db, session_id=session_id)
    if session_id and db_user:
        yield db_user
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="ユーザー認証に失敗しました。")
