from sqlalchemy import String, INTEGER
from sqlalchemy.orm import Mapped, mapped_column

from .Base import Base


class ExtUsers(Base):
    __tablename__ = "ext_users"

    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    username: Mapped[str] = mapped_column(String(30), nullable=True)
    name: Mapped[str] = mapped_column(String(50), nullable=True)
    surname: Mapped[str] = mapped_column(String(50), nullable=True)
    phone: Mapped[int] = mapped_column(INTEGER, nullable=True)
