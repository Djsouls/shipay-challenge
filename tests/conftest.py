import pytest

from datetime import date

from shipay.app_factory import create_app
from shipay.extensions import db
from shipay.models import UserModel, RoleModel

@pytest.fixture(scope='module')
def app():
    """Instância da aplicação principal do Flask"""
    app = create_app()

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/dev.db'

    with app.app_context():
        db.create_all()
        populate_db(db)
        yield app

        db.drop_all()

def populate_db(db):
    db.session.add(RoleModel(description='Gerente'))
    db.session.add(RoleModel(description='Desenvolvedor'))
    db.session.add(RoleModel(description='QA'))

    db.session.add(UserModel(
        name='Meu nome',
        email='meu@email.com',
        password='minha_senha',
        role_id=1,
        created_at=date.today(),
        updated_at=date.today()
    ))
    db.session.add(UserModel(
        name='José da silva',
        email='meu@email2.com',
        password='senhasenha',
        role_id=2,
        created_at=date.today(),
        updated_at=date.today()
    ))

    db.session.commit()
