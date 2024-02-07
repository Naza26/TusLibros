from system.internal_system import InternalCartSystem


class ExternalCartSystem:
    def __init__(self):
        self.system = InternalCartSystem()

    def create_cart(self, client_id, password):
        return self.system.create_cart(client_id, password)

    def add_to_cart(self, cart_id, book_isbn, book_quantity):
        return self.system.add_to_cart(cart_id, book_isbn, book_quantity)

    def list_cart(self, client_id):
        return self.system.list_cart(client_id)
