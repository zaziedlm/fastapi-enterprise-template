from app.models.user import UserORM

class UserService:
    def __init__(self, db):
        self.db = db

    def get_user(self, user_id: int):
        return self.db.query(UserORM).filter(UserORM.id == user_id).first()
