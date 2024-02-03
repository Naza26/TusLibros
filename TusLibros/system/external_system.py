from system.internal_system import InternalCartSystem


class ExternalCartSystem:
    def __init__(self):
        self.system = InternalCartSystem()

    def create_cart(self, client_id, password):

        return self.system.create_cart(client_id, password)