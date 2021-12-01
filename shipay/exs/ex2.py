from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from shipay.models import (
    UserModel,
    RoleModel,
    ClaimModel,
    UserClaimModel
)

DB_PATH = 'YOUR_DB_PATH'

engine = create_engine(DB_PATH)

user_id = 2

with Session(engine) as session:
    r = session.query(
            UserModel.id,
            UserModel.email,
            UserModel.password,
            ClaimModel.decription,
            RoleModel.description
        ).filter(
            UserModel.id == UserClaimModel.user_id
        ).filter(
            UserClaimModel.claim_id == ClaimModel.id
        ).filter(
            UserModel.role_id == RoleModel.id
        ).filter(
            UserModel.id == user_id
        ).all()
