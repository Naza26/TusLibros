from business.cart import Cart


class InternalCartSystem:
    SUCCESS_RESPONSE = "OK"

    def __init__(self):
        self._cart = None

    def create_cart(self, client_id, password):
        self._validate_cart_creation_parameters(client_id, password)

        self._cart = Cart()

        return 1

    def add_to_cart(self, cart_id, book_isbn, book_quantity):
        self._validate_cart_addition_parameters(cart_id, book_isbn, book_quantity)

        self._cart.add_book(book_isbn)

        return self.SUCCESS_RESPONSE

    def cart_exists_with(self, cart_id):
        return self._cart is not None

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
