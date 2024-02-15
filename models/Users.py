from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from .Base import Base


class Users(Base):
    __tablename__ = "users"

    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    email: Mapped[str] = mapped_column(nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
