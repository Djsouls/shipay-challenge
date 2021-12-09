from shipay.db.repositories import RoleRepository

from shipay.exceptions import MalformattedRequestError

class RoleController:
    def __init__(self):
        self.repository = RoleRepository()

    def add(self, description):
        if description is None:
            raise MalformattedRequestError
        self.repository.add_role(description)

    def get(self):
        return self.repository.get_all_roles()
