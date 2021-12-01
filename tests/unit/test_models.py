from shipay.models import (
    UserModel,
    RoleModel,
    ClaimModel,
    UserClaimModel
)

def test_user_model_creation():
    """Testa a criação de um usuário a partir do nosso modelo"""
    name = 'Meu nome'
    email = 'meu@email.com'
    password = 'minha_senha'
    role = 3

    user = UserModel(
                name=name,
                email=email,
                password=password,
                role_id=role
            )

    assert user.name == name
    assert user.email == email
    assert user.password == password
    assert user.role_id == role

def test_role_model_creation():
    """Testa a criação de uma role a partir do nosso modelo"""
    description = 'Gerente'

    role = RoleModel(description=description)

    assert role.description == description

def test_claim_model_creation():
    """Testa a criação de uma claim a partir do nosso modelo"""

    description = 'claims'
    active = True

    claim = ClaimModel(decription=description, active=active)

    assert claim.decription == description
    assert claim.active == active

def test_user_claim_model_creation():
    """Testa a criação de uma user_claim a partir do nosso modelo"""
    user_id = 4
    claim_id = 4

    user_claim = UserClaimModel(user_id=user_id, claim_id=claim_id)

    assert user_claim.user_id == user_id
    assert user_claim.claim_id == claim_id
