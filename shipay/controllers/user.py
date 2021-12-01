from typing import Dict, Union

from hashlib import sha256

from shipay.exceptions import MalformattedRequestError
from shipay.db.repositories import UserRepository
from shipay.utils.password_generator import generate_password

class UserController:
    def __init__(self):
        self.repository = UserRepository()
        self.encoding = 'utf-8'

    def add(self, user: Dict[str, Union[str, int]]):
        if (
            user['name'] is None or
            user['email'] is None or
            user['role'] is None
        ):
            raise MalformattedRequestError


        if user['password'] is None:
            user['password'] = generate_password()

        user['password'] = sha256(bytes(user['password'], self.encoding)).hexdigest()

        r = self.repository.add_user(
            name = user['name'],
            email = user['email'],
            password = user['password'],
            role_id = int(user['role'])
        )

    def get(self):
        return self.repository.get()

    def get_role(self, user_id: int):
        r = self.repository.get_role(user_id)

        if r is None:
            return r

        return list(r)
