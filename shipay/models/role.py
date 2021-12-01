from dataclasses import dataclass

from shipay.extensions import db

@dataclass
class RoleModel(db.Model):
    __tablename__ = 'roles'

    id: int = db.Column(db.Integer, db.Identity(), primary_key=True)
    description: str = db.Column(db.String, nullable=False)
