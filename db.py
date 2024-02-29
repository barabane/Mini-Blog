import random
import string
from math import ceil

from loguru import logger
from sqlalchemy import create_engine, select, delete
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker
from werkzeug.security import generate_password_hash

from models.BaseModel import Base
from models.Comments import Comments
from models.Posts import Posts
from models.Tags import Tags
from models.Users import Users


class DB:
    def __init__(self):
        try:
            self.metadata = Base.metadata
            self.engine = create_engine("sqlite:///miniblog.db")
            self.session = sessionmaker(bind=self.engine)()
            self.metadata.create_all(bind=self.engine)

        except Exception as ex:
            logger.error("При создании таблиц что-то пошло не так -> ")
            logger.error(ex)

    @staticmethod
    def generate_username(email: str):
        random.seed(email)
        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
        return 'user_' + random_string

    def get_user_by_email(self, email: str):
        user = self.session.scalar(select(Users).where(Users.email.is_(email)))
        return user

    def get_user_by_id(self, user_id: str):
        user = self.session.get(Users, user_id)
        return user or False

    def get_user_by_username(self, username: str):
        user = self.session.scalar(select(Users).where(Users.username.is_(username)))
        return user or False

    def update_user(self):
        self.session.commit()

    def register_user(self, email: str, password: str):
        try:
            new_user = Users(
                email=email,
                username=self.generate_username(email),
                password=generate_password_hash(password=password, method='scrypt', salt_length=5)
            )

            self.session.add(new_user)
            self.session.commit()
            return new_user
        except IntegrityError:
            self.register_user(email, password)

    def get_post(self, post_id: str):
        post = self.session.get(Posts, post_id)
        return post or False

    def get_limit_posts(self, limit: int = 0, page: int = 0):
        posts = self.session.execute(select(Posts).offset((page - 1) * limit).limit(limit)).scalars()
        # return posts.all()
        return False

    def get_all_hashtags(self):
        hashtags = self.session.scalars(select(Tags))
        return hashtags.all()

    def get_pages_count(self):
        return ceil(self.session.query(Posts).count() / 5)

    def get_post_hashtags(self, post_id: str):
        hashtags = self.session.scalars(select(Tags).where(Tags.post_id.is_(post_id)))
        return hashtags

    def get_user_posts(self, user_id: str):
        posts = self.session.scalars(select(Posts).where(Posts.author_id.is_(user_id)))
        return posts.all()

    def create_post(self, text: str, title: str, author_id: str, hashtags=""):
        new_post = Posts(
            text=text,
            title=title,
            author_id=author_id,
        )

        self.session.add(new_post)
        self.session.flush()

        new_hashtags = []
        for hashtag in hashtags.lower().split():
            new_hashtags.append(Tags(
                post_id=new_post.id,
                tag=hashtag
            ))

        self.session.add_all(new_hashtags)
        self.session.commit()

    def get_all_post_comments(self, post_id: str):
        post_comments = self.session.scalars(select(Comments).where(Comments.post_id.is_(post_id)))
        return post_comments

    def create_comment(self, text: str, post_id: str, author_id: str):
        new_comment = Comments(
            comment=text,
            post_id=post_id,
            author_id=author_id
        )

        self.session.add(new_comment)
        self.session.commit()

    def delete_post(self, post_id: str):
        self.session.execute(delete(Posts).where(Posts.id.is_(post_id)))
        self.session.commit()


db = DB()