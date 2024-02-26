import datetime
import uuid
from typing import Annotated

from sqlalchemy import String, DateTime
from sqlalchemy.orm import DeclarativeBase, mapped_column
from sqlalchemy.sql import func


def generate_uuid():
    return str(uuid.uuid4())


uuid_pk = Annotated[str, mapped_column(String(36), primary_key=True, default=generate_uuid)]
time_now = Annotated[datetime.datetime, mapped_column(DateTime(timezone=True), default=datetime.datetime.now(),
                                                      server_default=func.now())]


class Base(DeclarativeBase):
    pass