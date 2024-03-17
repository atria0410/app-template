from faker import Factory
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from models import UserModel

fake = Factory.create("ja_JP")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create_users_seed(db: Session, record_count: int = 100):
    print(f"\033[92mSeeding user data...\033[0m")

    for _ in range(record_count):
        db_user = UserModel(
            email=fake.email(),
            hashed_password=pwd_context.hash("password"),
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            birthday=fake.date_of_birth(),
        )
        db.add(db_user)
    db.commit()
