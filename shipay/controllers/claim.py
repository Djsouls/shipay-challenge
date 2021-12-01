from shipay.db.repositories import ClaimRepository

class ClaimController:
    def __init__(self):
        self.repository = ClaimRepository()
