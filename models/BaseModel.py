import datetime
from uuid import uuid4
from typing import Annotated
from sqlalchemy.sql import func
from sqlalchemy.orm import DeclarativeBase, mapped_column
from sqlalchemy import String, DateTime


def generated_uuid():
    return str(uuid4())


str_pk = Annotated[str, mapped_column(String(36), default=generated_uuid(), primary_key=True)]
time_now = Annotated[datetime.datetime, mapped_column(DateTime(timezone=True), server_default=func.now())]


class Base(DeclarativeBase):
    pass