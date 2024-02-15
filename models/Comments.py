import datetime

from sqlalchemy import ForeignKey, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func

from .Base import Base


class Comments(Base):
    __tablename__ = "comments"

    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    comment: Mapped[str] = mapped_column(nullable=False)
    post_id: Mapped[str] = mapped_column(String(50), ForeignKey("posts.id"), nullable=False)
    author_id: Mapped[str] = mapped_column(String(50), ForeignKey("users.id"), nullable=False)
    date: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
