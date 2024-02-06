from .Base import Base
from sqlalchemy import Column, VARCHAR, TEXT


class User(Base):
    __tablename__ = "user"

    id = Column(TEXT, primary_key=True, nullable=False)
    email = Column(VARCHAR(30), nullable=False)
    password = Column(VARCHAR(40), nullable=False)