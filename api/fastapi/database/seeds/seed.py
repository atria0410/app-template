import users
from sqlalchemy.orm import Session

from database.database import get_db_session


def seed(db: Session):
    users.create_users_seed(db=db)


if __name__ == "__main__":
    SessionLocal = get_db_session()
    db = SessionLocal()
    seed(db=db)
    db.close
