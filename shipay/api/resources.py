from flask import Blueprint, request, Response, jsonify

from shipay.exceptions import MalformattedRequestError

from shipay.controllers import UserController, RoleController

bp = Blueprint('api', __name__, url_prefix='/api/v1')

user_controller = UserController()
role_controller = RoleController()

@bp.route('/')
def hello_world():
    return 'Hello World!', 200

@bp.route('/user_role/<int:user_id>', methods=['GET'])
def get_user_role_by_id(user_id):
    """ Rota para retorna o role_id de um usuário a partir do user_id
        get:
          description: Retorna um role_id a partir de user_id
          parameters:
            - name: user_id
              in: path
              description: ID do usuário
              type: integer
              required: true
          responses:
            200:
              description: role_id retornado
            204:
              description: role_id não encontrado
    """
    r = user_controller.get_role(user_id)

    if r is None:
        return jsonify({}), 204

    return jsonify(user_controller.get_role(user_id))

@bp.route('/user', methods=['POST'])
def add_user():
    """ Rota para adicionar um usuário a partir das
        informações passadas pelo json.
        post:
          description: Rota para realizar a adição de um usuário
          requestBody:
            required: True
            content:
              application/json
          responses:
            '200':
              descritpion: Adicionou o usuário com sucesso
                content:
                  application/json
            '400':
              description: Request mal formatada, provavelmente campos faltantes no JSON
               content:
                 application/json
    """
    user = {
        'name': request.json.get('name'),
        'email': request.json.get('email'),
        'password': request.json.get('password'),
        'role': request.json.get('role')
    }

    try:
        user_controller.add(user)
    except MalformattedRequestError: 
        return jsonify(
            success=False,
            error='Malformatted request, fields missing'
        ), 400

    return jsonify(success=True)

@bp.route('/user', methods=['GET'])
def show_users():
    return jsonify(user_controller.get())

@bp.route('/role', methods=['POST'])
def create_role():
    try:
        role_controller.add(request.json.get('description'))
    except MalformattedRequestError:
        return jsonify(
            success=False,
            error='Malformatted request, fields missing'
        ), 400

    return jsonify(success=True)

@bp.route('/roles', methods=['GET'])
def show_roles():
    return jsonify(role_controller.get())
