from system.internal_system import InternalCartSystem


class ExternalCartSystem:
    def __init__(self):
        self.system = InternalCartSystem()

    def create_cart(self, request):
        params = request.http_post_parameters_for('/createCart')
        client_id = params.get('client_id')
        password = params.get('password')

        self._validate_cart_creation_parameters(client_id, password)

        return self.system.create_cart(client_id, password)

    def add_to_cart(self, request):
        params = request.http_post_parameters_for('/addToCart')
        cart_id = params.get('cart_id')
        book_isbn = params.get('book_isbn')
        book_quantity = params.get('book_quantity')

        self._validate_cart_addition_parameters(cart_id, book_isbn, book_quantity)

        return self.system.add_to_cart(cart_id, book_isbn, book_quantity)

    def list_cart(self, request):
        params = request.http_post_parameters_for('/listCart')
        client_id = params.get('client_id')

        self._validate_cart_listing_parameters(client_id)

        return self.system.list_cart(client_id)

    def _validate_cart_creation_parameters(self, client_id, password):
        self._validate_parameter(client_id, "Client ID")
        self._validate_parameter(password, "Password")

    def _validate_cart_addition_parameters(self, cart_id, book_isbn, book_quantity):
        self._validate_parameter(cart_id, "Cart ID")
        self._validate_parameter(book_isbn, "Book ISBN")
        self._validate_parameter(book_quantity, "Book Quantity")

    def _validate_cart_listing_parameters(self, client_id):
        self._validate_parameter(client_id, "Client ID")

    def _validate_parameter(self, parameter, parameter_name):
        if parameter is None:
            raise ValueError(f'{parameter_name} is missing')
