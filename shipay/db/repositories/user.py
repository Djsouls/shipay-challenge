from datetime import date

from shipay.extensions import db

from shipay.models import UserModel

class UserRepository:
    def __init__(self):
        self.model = UserModel

    def add_user(self, name: str, email: str, password: str, role_id: int):
        user = UserModel(
            name = name,
            email = email,
            password = password,
            role_id = role_id,
            created_at = date.today(),
            updated_at = date.today()
        )

        db.session.add(user)
        db.session.commit()

    def get(self):
        return self.model.query.all()

    def get_role(self, user_id: int):
        return self.model.query.with_entities(self.model.role_id).filter_by(id=user_id).first()
