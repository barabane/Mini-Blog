from typing import Optional
from sqlalchemy import String, INTEGER, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from .BaseModel import Base


class ExtUsers(Base):
    __tablename__ = "ext_users"

    id: Mapped[Optional[str]] = mapped_column(String(36), ForeignKey("users.id"), primary_key=True)
    username: Mapped[Optional[str]] = mapped_column(String(30))
    name: Mapped[Optional[str]] = mapped_column(String(50))
    surname: Mapped[Optional[str]] = mapped_column(String(50))
    phone: Mapped[Optional[str]] = mapped_column(INTEGER)
