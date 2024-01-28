from business.cart import Cart


class InternalCartSystem:
    def __init__(self):
        self.cart_system = {}

    def create_cart(self, client_id, password):
        self._validate_cart_creation_parameters(client_id, password)

        cart = Cart()
        cart_id = self._cart_id()
        self.cart_system[cart_id] = {'cart': cart, 'client_info': {'client_id': client_id, 'password': password}}

        return cart_id

    def add_to_cart(self, cart_id, book_isbn, book_quantity):
        self._validate_cart_addition_parameters(cart_id, book_isbn, book_quantity)

        cart = self.cart_system[cart_id]['cart']
        cart.add_book(book_isbn, book_quantity)

    def _cart_id(self):
        return len(self.cart_system) + 1

    def _validate_cart_creation_parameters(self, client_id, password):
        if client_id is None:
            raise ValueError('Client ID is missing')
        if password is None:
            raise ValueError('Password is missing')

    def _validate_cart_addition_parameters(self, cart_id, book_isbn, book_quantity):
        if cart_id is None:
            raise ValueError('Cart ID is missing')
        if book_isbn is None:
            raise ValueError('Book ISBN is missing')
        if book_quantity is None:
            raise ValueError('Book quantity is missing')
