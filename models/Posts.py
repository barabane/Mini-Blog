from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from .BaseModel import Base, time_now, uuid_pk


class Posts(Base):
    __tablename__ = "posts"

    id: Mapped[uuid_pk]
    title: Mapped[str] = mapped_column(nullable=False)
    text: Mapped[str] = mapped_column(nullable=False)
    author_id: Mapped[str] = mapped_column(String(36), ForeignKey("users.id"), nullable=False)
    created_at: Mapped[time_now]
    updated_at: Mapped[time_now]
