import uuid
from datetime import datetime

from loguru import logger
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from werkzeug.security import generate_password_hash

# models
from models.Base import Base
from models.Comments import Comments
from models.Posts import Posts
from models.Users import Users


class DB:
    def __init__(self):
        try:
            self.metadata = Base.metadata
            self.engine = create_engine("sqlite:///miniblog.db", echo=True)
            self.session = sessionmaker(bind=self.engine)()
            self.metadata.create_all(bind=self.engine)

        except Exception as ex:
            logger.error("При создании таблиц что-то пошло не так -> ")
            logger.error(ex)

    def get_user_by_email(self, email: str):
        user = self.session.scalar(select(Users).where(Users.email.is_(email)))
        return user

    def get_user_by_id(self, user_id: str):
        user = self.session.scalar(select(Users).where(Users.id.is_(user_id)))
        if not user:
            return False

        return user

    def register_user(self, email: str, password: str):
        new_user = Users(id=str(uuid.uuid4()), email=email,
                         password=generate_password_hash(password=password, method='scrypt', salt_length=5))
        # insert(Users).values(id=str(uuid.uuid4()), email=email,
        #                  password=generate_password_hash(password=password, method='scrypt', salt_length=5))

        self.session.add(new_user)
        self.session.commit()
        return new_user

    def get_post(self, post_id: str):
        post = self.session.scalar(select(Posts).where(Posts.id.is_(post_id)))

        return post

    def get_all_posts(self):
        posts = self.session.scalars(select(Posts))
        return posts

    def get_user_posts(self, user_id: str):
        posts = self.session.scalars(select(Posts).where(Posts.author_id.is_(user_id)))
        return posts.all()

    def create_post(self, text: str, title: str, author_id: str, theme: str = ""):
        new_post = Posts(
            id=str(uuid.uuid4()),
            text=text,
            title=title,
            theme=theme,
            author_id=author_id,
            date=datetime.now()
        )

        self.session.add(new_post)
        self.session.commit()

    def get_all_post_comments(self, post_id: str):
        post_comments = self.session.scalars(select(Comments).where(Comments.post_id.is_(post_id)))

        return post_comments

    def create_comment(self, text: str, post_id: str, author: str):
        new_comment = Comments(
            id=str(uuid.uuid4()),
            comment=text,
            post_id=post_id,
            author=author
        )

        self.session.add(new_comment)
        self.session.commit()


db = DB()
