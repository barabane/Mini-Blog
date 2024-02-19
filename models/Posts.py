from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from .BaseModel import Base, str_pk, time_now


class Posts(Base):
    __tablename__ = "posts"

    id: Mapped[str_pk]
    text: Mapped[str] = mapped_column(nullable=False)
    title: Mapped[str] = mapped_column(nullable=False)
    theme: Mapped[str] = mapped_column(String(50), nullable=True)
    author_id: Mapped[str] = mapped_column(String(36), ForeignKey("users.id"), nullable=False)
    date: Mapped[time_now]
