from sqlalchemy import Column, TEXT, ForeignKey, VARCHAR, DATETIME

from .Base import Base


class Comment(Base):
    __tablename__ = "comment"

    id = Column(TEXT, primary_key=True)
    comment = Column(TEXT, nullable=False)
    post_id = Column(TEXT, ForeignKey("post.id"), nullable=False)
    author = Column(VARCHAR(30), ForeignKey("user.email"), nullable=False)
    date = Column(DATETIME)
