from dataclasses import dataclass
from datetime import datetime

from shipay.extensions import db

@dataclass
class UserModel(db.Model):
    __tablename__ = 'users'

    id: int = db.Column(db.Integer, db.Identity(), primary_key=True,
            nullable=False)
    name: str = db.Column(db.String(), nullable=False)
    email: str = db.Column(db.String(), nullable=False)
    password: str = db.Column(db.String(), nullable=False)
    role_id: int = db.Column(db.Integer, db.ForeignKey('roles.id'),
            nullable=False)
    created_at: datetime = db.Column(db.DateTime, nullable=False)
    updated_at: datetime = db.Column(db.DateTime, nullable=False)
