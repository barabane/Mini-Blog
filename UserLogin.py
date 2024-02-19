from db import db, Users


class UserLogin:
    def __init__(self):
        self.__user = None
        self.id = None
        self.email = None

    def create(self, user: Users):
        self.__user = user
        return self

    def get_user_from_db(self, user_id):
        self.__user = db.get_user_by_id(user_id=user_id)

        if self.__user:
            self.id = self.__user.id
            self.email = self.__user.email

        return self

    @staticmethod
    def is_authenticated():
        return True

    @staticmethod
    def is_active():
        return True

    @staticmethod
    def is_anonymous():
        return False

    def get_id(self):
        return str(self.__user.id)
