from shipay.models import RoleModel

from shipay.extensions import db

class RoleRepository:
    def __init__(self):
        self.model = RoleModel

    def add_role(self, description):
        role = RoleModel(description=description)

        db.session.add(role)
        db.session.commit()

    def get_all_roles(self):
        return self.model.query.all()
