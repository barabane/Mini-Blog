from db import db, User


class UserLogin:
    def __init__(self):
        self.id = None
        self.email = None

    def create(self, user: User):
        self.__user = user
        return self

    def get_user_from_db(self, user_id):
        self.__user = db.get_user_by_id(user_id=user_id)
        self.id = self.__user.id
        self.email = self.__user.email
        return self

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.__user.id)
