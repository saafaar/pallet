class AgreementUseCase:

    def __init__(self, match, cargo, count):
        self.freight_id = match.freight_id
        self.cargo_id = match.cargo_id
        self.count = count
        self.price = cargo.price * self.count
