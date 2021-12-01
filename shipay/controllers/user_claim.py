from shipay.db.repositories import UserClaimRepository

class UserClaimController:
    def __init__(self):
        self.repository = UserClaimRepository()
