from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from .BaseModel import Base, str_pk, time_now


class Comments(Base):
    __tablename__ = "comments"

    id: Mapped[str_pk]
    comment: Mapped[str] = mapped_column(nullable=False)
    post_id: Mapped[str] = mapped_column(String(50), ForeignKey("posts.id"), nullable=False)
    author_id: Mapped[str] = mapped_column(String(50), ForeignKey("users.id"), nullable=False)
    date: Mapped[time_now]
