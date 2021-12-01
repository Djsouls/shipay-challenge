from dataclasses import dataclass

from shipay.extensions import db

@dataclass
class UserClaimModel(db.Model):
    __tablename__ = 'user_claims'

    user_id: int = db.Column(db.Integer, db.ForeignKey('users.id'),
            nullable=False)
    claim_id: int = db.Column(db.Integer, db.ForeignKey('claims.id'),
            nullable=False)

    # SQLAlchemy não aceita criação de modelos que não possuam
    # pelo menos uma primary key. Então, optou-se por fazer
    # primary composta de ambas colunas, o que, na prática
    # não alterará o comportamento desejado.

    __table_args__ = (
        db.PrimaryKeyConstraint(user_id, claim_id),
    )
