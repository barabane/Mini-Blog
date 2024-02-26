from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from .BaseModel import Base


class Tags(Base):
    __tablename__ = "tags"

    id: Mapped[int] = mapped_column(String(36), primary_key=True)
    post_id: Mapped[str] = mapped_column(String(36), ForeignKey("posts.id"), nullable=False)
    tag: Mapped[str] = mapped_column(String(15), nullable=False)
