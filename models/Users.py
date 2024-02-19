from sqlalchemy.orm import Mapped, mapped_column
from .BaseModel import Base, str_pk


class Users(Base):
    __tablename__ = "users"

    id: Mapped[str_pk]
    email: Mapped[str] = mapped_column(nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
