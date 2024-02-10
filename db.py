import uuid
from datetime import datetime

from loguru import logger
from sqlalchemy import create_engine, select
from sqlalchemy.orm import create_session
from werkzeug.security import generate_password_hash

# models
from models.Base import Base
from models.Comment import Comment
from models.Post import Post
from models.User import User


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

    def get_post(self, post_id: str):
        post = self.session.scalar(select(Post).where(Post.id.is_(post_id)))

        return post

    def get_all_posts(self):
        posts = self.session.scalars(select(Post))
        return posts

    def get_user_posts(self, user_email: str):
        posts = self.session.scalars(select(Post).where(Post.author.is_(user_email)))
        return posts.all()

    def create_post(self, text: str, title: str, author: str, theme: str = ""):
        new_post = Post(
            id=str(uuid.uuid4()),
            text=text,
            title=title,
            theme=theme,
            author=author,
            date=datetime.now()
        )

        self.session.add(new_post)
        self.session.commit()

    def get_all_post_comments(self, post_id: str):
        post_comments = self.session.scalars(select(Comment).where(Comment.post_id.is_(post_id)))

        return post_comments

    def create_comment(self, text: str, post_id: str, author: str):
        new_comment = Comment(
            id=str(uuid.uuid4()),
            comment=text,
            post_id=post_id,
            author=author
        )

        self.session.add(new_comment)
        self.session.commit()


db = DB()
