from passlib.context import CryptContext
from sqlalchemy.orm import Session

from models import UserModel
from schemas import UserSchema

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(UserModel).offset(skip).limit(limit).all()


def get_user(db: Session, user_id: int):
    return db.query(UserModel).filter(UserModel.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(UserModel).filter(UserModel.email == email).first()


def get_user_by_session_id(db: Session, session_id: str):
    return db.query(UserModel).filter(UserModel.session_id == session_id).first()


def get_user_by_email_and_password(db: Session, email: str, password: str):
    db_user = get_user_by_email(db, email=email)
    if db_user and pwd_context.verify(password, db_user.hashed_password):
        return db_user
    else:
        return None


def create_user(db: Session, user: UserSchema.UserCreate):
    db_user = UserModel(
        email=user.email,
        hashed_password=pwd_context.hash(user.password),
        first_name=user.first_name,
        last_name=user.last_name,
        birthday=user.birthday,
    )
    db.add(db_user)
    db.flush()
    db.refresh(db_user)
    return db_user


def update_user(db: Session, user_id: int, user: UserSchema.UserUpdate):
    db_user = get_user(db, user_id=user_id)
    if not db_user:
        return None
    db_user.email = user.email
    db_user.hashed_password = pwd_context.hash(user.password)
    db_user.first_name = user.first_name
    db_user.last_name = user.last_name
    db_user.birthday = user.birthday
    db_user.is_active = user.is_active
    db.flush()
    db.refresh(db_user)
    return db_user


def delete_user(db: Session, user_id: int):
    db_user = get_user(db, user_id=user_id)
    if not db_user:
        return None
    db.delete(db_user)
    db.flush()
    return db_user


def set_session_id(db: Session, user_id: int, session_id: str):
    db_user = get_user(db, user_id=user_id)
    db_user.session_id = session_id
    db.flush()
    db.refresh(db_user)
    return db_user


def drop_session_id(db: Session, session_id: str):
    db_user = get_user_by_session_id(db, session_id=session_id)
    db_user.session_id = None
    db.flush()
    db.refresh(db_user)
    return db_user
