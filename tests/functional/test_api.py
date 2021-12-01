BASE_API = '/api/v1/'
TEST_USER_ID = 2
INVALID_USER_ID = 0

def test_invalid_url_return_404(client):
    """Testa se uma URL inválida retorna 404"""
    assert client.get('/url_que_nao_existe').status_code == 404

def test_valid_url_return_200(client):
    """Testa se uma URL válida retorna 200"""
    assert client.get(BASE_API).status_code == 200

def test_add_role_malformatted_request(client):
    """Testa se uma request inválida para a rota de adição de role retorna um erro"""
    route_url = BASE_API + 'role'

    rv = client.post(route_url,
        json={}
    )

    json = rv.get_json()

    assert rv.status_code == 400
    assert 'error' in json
    assert json['success'] == False

def test_malformatted_request_to_add_user(client):
    """Testa se uma request inválida para a rota de adição de usuário retorna um erro"""
    route_url = BASE_API + 'user'
    
    invalid_users = [
        {   # Faltando o campo role
            'name': 'Meu nome',
            'email': 'meu@email.com',
            'password': 'minha_senha'
        },
        {   # Faltando o campo name
            'email': 'meu@email.com',
            'password': 'minha_senha',
            'role': 5
        },
        {   # Faltando o campo email
            'name': 'Meu nome',
            'password': 'minha_senha',
            'role': 5
        }
    ]

    for invalid_user in invalid_users:
        rv = client.post(route_url,
            json=invalid_user
        )

        assert rv.status_code == 400
    
        json = rv.get_json()

        assert 'error' in json
        assert json['success'] == False

def test_method_not_allowed_to_user_role(client):
    """Testa se o método POST é inválidp para a rota user_role"""
    route_url = BASE_API + 'user_role/' + str(TEST_USER_ID)

    rv = client.post(route_url)

    assert rv.status_code == 405

def test_valid_user_add_with_password(client):
    """Testa se a adição de um usuário válido com o campo senha funciona"""
    route_url = BASE_API + 'user'
    user_data = {
        'name': 'Meu nome',
        'email': 'meu@email.com',
        'password': 'minhasenha',
        'role': 5
    }

    rv = client.post(route_url,
         json=user_data
    )
    
    json = rv.get_json()

    assert rv.status_code == 200
    assert json['success'] == True

def test_valid_user_add_without_password(client):
    """Testa se a adição de um usuário válido sem o cmapo senha funciona"""
    route_url = BASE_API + 'user'
    user_data = {
        'name': 'Meu nome',
        'email': 'meu@email.com',
        'role': 5
    }

    rv = client.post(route_url,
         json=user_data
    )

    json = rv.get_json()

    assert rv.status_code == 200
    assert json['success'] == True

def test_user_role_for_valid_user_returns_200(client):
    """Testa se a rota user_role funciona corretamente"""
    route_url = BASE_API + 'user_role/' + str(TEST_USER_ID)

    rv = client.get(route_url)
    json = rv.get_json()

    assert rv.status_code == 200
    assert len(json) == 1

def test_user_role_for_empty_reponse_return_204(client):
    """Testa se a rota user_role retorna 204 e json vazio caso o usuário não exista"""
    route_url = BASE_API + 'user_role/' + str(INVALID_USER_ID)

    rv = client.get(route_url)

    assert rv.status_code == 204
