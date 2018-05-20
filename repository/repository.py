#TODO Csinálj valami repót

import uuid

class MemRepo:
    def __init__(self):
        self.cargo = []
        self.freight = []
        self.match = []
        self.agreement = []

    def add_cargo(self, cargo, psid):
        id = uuid.uuid4()
        cargo.append([id, cargo, psid])

    def add_freight(self, freight, psid):
        id = uuid.uuid4()
        freight.append([id, freight, psid])

    def add_match(self, match):
        id = uuid.uuid4()
        match.append([id, match])

    def add_agreement(self, agreement):
        id = uuid.uuid4()
        agreement.append([id, agreement])