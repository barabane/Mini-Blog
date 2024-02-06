from .Base import Base
from sqlalchemy.sql import func
from sqlalchemy import Column, VARCHAR, TEXT, ForeignKey, DATETIME


class Post(Base):
    __tablename__ = "post"

    id = Column(TEXT, primary_key=True, nullable=False)
    text = Column(TEXT, nullable=False)
    title = Column(VARCHAR(100), nullable=False)
    author_id = Column(TEXT, ForeignKey("user.id"))
    theme = Column(VARCHAR(30))
    date = Column(DATETIME)
