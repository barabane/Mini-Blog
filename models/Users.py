from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from models.BaseModel import Base, uuid_pk, time_now


class Users(Base):
    __tablename__ = "users"

    id: Mapped[uuid_pk]
    username: Mapped[str] = mapped_column(String(20), nullable=False, unique=True)
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    password: Mapped[str] = mapped_column(nullable=False)
    about: Mapped[str] = mapped_column(String(200), nullable=True, default="")
    reg_date: Mapped[time_now]
