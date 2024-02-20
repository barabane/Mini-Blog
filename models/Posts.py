from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from .BaseModel import Base, time_now


class Posts(Base):
    __tablename__ = "posts"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, nullable=False)
    text: Mapped[str] = mapped_column(nullable=False)
    title: Mapped[str] = mapped_column(nullable=False)
    author_id: Mapped[str] = mapped_column(String(36), ForeignKey("users.id"), nullable=False)
    date: Mapped[time_now]
