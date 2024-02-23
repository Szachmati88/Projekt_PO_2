import datetime as dt

class UserLogic:
    def __init__(self, db):
        self.year = dt.date.year
        self.db = db

    def get_users(self):
        return self.db.get_all_users()

    def get_user(self, user_id):
        return self.db.get_user_by_id(user_id)

    def create_user(self, data,):
        return self.db.create_user(data), self.year

    def update_user(self, user_id, data):
        return self.db.update_user(user_id, data)

    def delete_user(self, user_id):
        return self.db.delete_user(user_id)
