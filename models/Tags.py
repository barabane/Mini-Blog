from sqlalchemy import String, INTEGER
from sqlalchemy.orm import Mapped, mapped_column

from .BaseModel import Base


class Tags(Base):
    __tablename__ = "tags"

    id: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    post_id: Mapped[str] = mapped_column(String(36), nullable=False)
    tag: Mapped[str] = mapped_column(String(30), nullable=False)
