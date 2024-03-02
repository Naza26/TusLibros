from http_protocol.response import Response
from system.internal_system import InternalCartSystem


class ExternalCartSystem:
    def __init__(self):
        self.system = InternalCartSystem()

    def create_cart(self, request):
        params = request.http_post_parameters_for('/createCart')
        client_id = params.get('client_id')
        password = params.get('password')

        body = self._validate_parameter(client_id, 'Client ID')

        if body is not None:
            return Response(Response.BAD_REQUEST_RESPONSE, body)

        body = self._validate_parameter(password, 'Password')

        if body is not None:
            return Response(Response.BAD_REQUEST_RESPONSE, body)

        body = {'objects': self.system.create_cart(client_id, password)}

        return Response(Response.OK_RESPONSE, body)

    def add_to_cart(self, request):
        params = request.http_post_parameters_for('/addToCart')
        cart_id = params.get('cart_id')
        book_isbn = params.get('book_isbn')
        book_quantity = params.get('book_quantity')

        self._validate_cart_addition_parameters(cart_id, book_isbn, book_quantity)

        body = self._validate_parameter(cart_id, 'Cart ID')

        if body is not None:
            return Response(Response.BAD_REQUEST_RESPONSE, body)

        body = self._validate_parameter(book_isbn, 'Book ISBN')

        if body is not None:
            return Response(Response.BAD_REQUEST_RESPONSE, body)

        body = self._validate_parameter(book_quantity, 'Book Quantity')

        if body is not None:
            return Response(Response.BAD_REQUEST_RESPONSE, body)

        self.system.add_to_cart(cart_id, book_isbn, book_quantity)

        return Response(Response.OK_RESPONSE, None)

    def list_cart(self, request):
        params = request.http_post_parameters_for('/listCart')
        client_id = params.get('client_id')

        body = self._validate_parameter(client_id, 'Client ID')

        if body is not None:
            return Response(Response.BAD_REQUEST_RESPONSE, body)

        body = {'books': self.system.list_cart(client_id)}

        return Response(Response.OK_RESPONSE, body)

    def _validate_cart_creation_parameters(self, client_id, password):
        self._validate_parameter(client_id, "Client ID")
        self._validate_parameter(password, "Password")

        body = {'errors': self.system.create_cart(client_id, password)}

    def _validate_cart_addition_parameters(self, cart_id, book_isbn, book_quantity):
        self._validate_parameter(cart_id, "Cart ID")
        self._validate_parameter(book_isbn, "Book ISBN")
        self._validate_parameter(book_quantity, "Book Quantity")

    def _validate_cart_listing_parameters(self, client_id):
        self._validate_parameter(client_id, "Client ID")

    def _validate_parameter(self, parameter, parameter_name):
        if parameter is None:
            return {'errors': f'1|{parameter_name} is missing'}
        return None
