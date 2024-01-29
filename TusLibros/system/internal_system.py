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
        self._validate_parameter(client_id, "Client ID")
        self._validate_parameter(password, "Password")

    def _validate_cart_addition_parameters(self, cart_id, book_isbn, book_quantity):
        self._validate_parameter(cart_id, "Cart ID")
        self._validate_parameter(book_isbn, "Book ISBN")
        self._validate_parameter(book_quantity, "Book Quantity")

    def _validate_parameter(self, parameter, parameter_name):
        if parameter is None:
            raise ValueError(f'{parameter_name} is missing')
