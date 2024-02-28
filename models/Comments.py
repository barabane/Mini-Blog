from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column
from models.BaseModel import Base, uuid_pk, time_now


class Comments(Base):
    __tablename__ = "comments"

    id: Mapped[uuid_pk]
    post_id: Mapped[str] = mapped_column(String(50), ForeignKey("posts.id"), nullable=False)
    text: Mapped[str] = mapped_column(nullable=False)
    author_id: Mapped[str] = mapped_column(String(36), ForeignKey("users.id"), nullable=False)
    created_at: Mapped[time_now]
    updated_at: Mapped[time_now]
