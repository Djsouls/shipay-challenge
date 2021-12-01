from dataclasses import dataclass

from shipay.extensions import db

@dataclass
class ClaimModel(db.Model):
    __tablename__ = 'claims'

    id: int = db.Column(db.Integer, db.Identity(), primary_key=True)
    decription: str = db.Column(db.String, nullable=False)
    active: bool = db.Column(db.Boolean, nullable=False, default=True)
