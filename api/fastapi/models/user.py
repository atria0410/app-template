from datetime import datetime

from sqlalchemy import BigInteger, Boolean, Column, Date, DateTime, String

from database.database import Base


class User(Base):
    __tablename__ = "users"
    __table_args__ = {"comment": "ユーザーマスタ"}

    id = Column(BigInteger, primary_key=True, comment="id")
    email = Column(String, unique=True, index=True, comment="メールアドレス")
    hashed_password = Column(String, comment="パスワードハッシュ")
    first_name = Column(String, nullable=False, comment="名前")
    last_name = Column(String, nullable=False, comment="苗字")
    birthday = Column(Date, comment="誕生日")
    is_active = Column(Boolean, default=True, comment="有効フラグ")
    session_id = Column(String, comment="セッションID")
    created_at = Column(DateTime, default=datetime.now(), nullable=False, comment="作成日時")
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now(), nullable=False, comment="更新日時")
    version = Column(BigInteger, nullable=False, comment="バージョン")

    __mapper_args__ = {"version_id_col": version}
