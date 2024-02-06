import uuid
from loguru import logger
from werkzeug.security import generate_password_hash
from sqlalchemy.orm import DeclarativeBase, create_session
from sqlalchemy import Column, VARCHAR, create_engine, select, TEXT


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "user"

    id = Column(TEXT, primary_key=True, nullable=False)
    email = Column(VARCHAR(30), nullable=False)
    password = Column(VARCHAR(40), nullable=False)


class DB:
    def __init__(self):
        try:
            self.engine = create_engine("sqlite:///miniblog.db", echo=True)
            self.session = create_session(bind=self.engine)

            Base.metadata.create_all(bind=self.engine)

        except Exception as ex:
            logger.error("При создании таблиц что-то пошло не так -> ", ex)

    def get_user_by_email(self, email: str):
        user = self.session.scalar(select(User).where(User.email.is_(email)))

        if not user:
            logger.error("Такой пользователь не найден")

        return user

    def get_user_by_id(self, user_id: int):
        user = self.session.scalar(select(User).where(User.id.is_(user_id)))

        if not user:
            return False

        return user

    def register_user(self, email: str, password: str):
        new_user = User(id=str(uuid.uuid4()), email=email, password=generate_password_hash(password=password,  method='scrypt', salt_length=5))

        self.session.add(new_user)
        self.session.commit()
        logger.info("Новый пользователь добавлен")
        return new_user


db = DB()
