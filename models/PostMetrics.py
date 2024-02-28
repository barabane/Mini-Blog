from sqlalchemy import String, ForeignKey, INTEGER
from sqlalchemy.orm import Mapped, mapped_column
from models.BaseModel import Base


class PostMetrics(Base):
    post_id: Mapped[str] = mapped_column(String(36), ForeignKey("posts.id"), nullable=False)
    views: Mapped[int] = mapped_column(INTEGER, default=0)
    likes: Mapped[int] = mapped_column(INTEGER, default=0)
