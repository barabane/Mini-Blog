from db import db, User


class UserLogin:
    def create(self, user: User):
        self.__user = user
        return self

    def get_user_from_db(self, user_id):
        self.__user = db.get_user_by_id(user_id=user_id)
        return self

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.__user.id)

