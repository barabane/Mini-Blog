from sqlalchemy import Column, VARCHAR, TEXT, ForeignKey, DATETIME

from .Base import Base


class Post(Base):
    __tablename__ = "post"

    id = Column(TEXT, primary_key=True, nullable=False)
    text = Column(TEXT, nullable=False)
    title = Column(VARCHAR(100), nullable=False)
    author = Column(VARCHAR(30), ForeignKey("user.email"), nullable=False)
    theme = Column(VARCHAR(30))
    date = Column(DATETIME)
