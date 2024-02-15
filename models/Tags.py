from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from .Base import Base


class Tags(Base):
    __tablename__ = "tags"

    post_id: Mapped[str] = mapped_column(String(36), ForeignKey("posts.id"), primary_key=True, nullable=False)
    tag: Mapped[str] = mapped_column(String(30), nullable=False)
