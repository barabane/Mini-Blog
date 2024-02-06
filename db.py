import uuid
from datetime import datetime
from loguru import logger
from werkzeug.security import generate_password_hash
from sqlalchemy.orm import create_session
from sqlalchemy import create_engine, select

# models
from models.Base import Base
from models.User import User
from models.Post import Post


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
        new_user = User(id=str(uuid.uuid4()), email=email,
                        password=generate_password_hash(password=password, method='scrypt', salt_length=5))

        self.session.add(new_user)
        self.session.commit()
        return new_user

    def get_post(self):
        pass

    def get_all_posts(self):
        posts = self.session.execute(select(User)).all()

        return posts

    def create_post(self, text: str, title: str, author_id: User.id, theme: str = ""):
        new_post = Post(
            id=str(uuid.uuid4()),
            text=text,
            title=title,
            theme=theme,
            author_id=author_id,
            date=datetime.now()
        )

        self.session.add(new_post)
        self.session.commit()


db = DB()
