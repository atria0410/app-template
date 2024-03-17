from datetime import date, datetime

from pydantic import BaseModel


class UserBase(BaseModel):
    email: str
    first_name: str
    last_name: str
    birthday: date


class User(UserBase):
    id: int
    is_active: bool
    created_at: datetime
    updated_at: datetime
    version: int

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    password: str


class UserUpdate(UserBase):
    password: str
    is_active: bool
