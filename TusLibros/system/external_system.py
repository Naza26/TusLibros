from http_protocol.response import Response
from system.internal_system import InternalSystem


class ExternalSystem:
    def __init__(self):
        self._system = InternalSystem()

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

        body = {'objects': self._system.create_cart(client_id, password)}

        return Response(Response.OK_RESPONSE, body)

    def add_to_cart(self, request):
        params = request.http_post_parameters_for('/addToCart')
        cart_id = params.get('cart_id')
        book_isbn = params.get('book_isbn')
        book_quantity = params.get('book_quantity')

        body = self._validate_parameter(cart_id, 'Cart ID')

        if body is not None:
            return Response(Response.BAD_REQUEST_RESPONSE, body)

        body = self._validate_parameter(book_isbn, 'Book ISBN')

        if body is not None:
            return Response(Response.BAD_REQUEST_RESPONSE, body)

        body = self._validate_parameter(book_quantity, 'Book Quantity')

        if body is not None:
            return Response(Response.BAD_REQUEST_RESPONSE, body)

        self._system.add_to_cart(cart_id, book_isbn, book_quantity)

        return Response(Response.OK_RESPONSE, None)

    def list_cart(self, request):
        params = request.http_post_parameters_for('/listCart')
        client_id = params.get('client_id')

        body = self._validate_parameter(client_id, 'Client ID')

        if body is not None:
            return Response(Response.BAD_REQUEST_RESPONSE, body)

        body = {'objects': self._system.list_cart(client_id)}

        return Response(Response.OK_RESPONSE, body)

    def checkout_cart(self, request):
        params = request.http_post_parameters_for('/checkoutCart')
        cart_id = params.get('cart_id')
        credit_card_number = params.get('credit_card_number')
        credit_card_expiration_date = params.get('credit_card_expiration_date')
        credit_card_owner = params.get('credit_card_owner')

        body = self._validate_parameter(cart_id, 'Cart ID')

        if body is not None:
            return Response(Response.BAD_REQUEST_RESPONSE, body)

        body = self._validate_parameter(credit_card_number, 'Credit Card Number')

        if body is not None:
            return Response(Response.BAD_REQUEST_RESPONSE, body)

        body = self._validate_parameter(credit_card_expiration_date, 'Credit Card Expiration Date')

        if body is not None:
            return Response(Response.BAD_REQUEST_RESPONSE, body)

        body = self._validate_parameter(credit_card_owner, 'Credit Card Owner')

        if body is not None:
            return Response(Response.BAD_REQUEST_RESPONSE, body)

        body = {'objects': self._system.checkout_cart(cart_id, credit_card_number, credit_card_expiration_date,
                                                      credit_card_owner)}

        return Response(Response.OK_RESPONSE, body)

    def list_purchases(self, request):
        params = request.http_post_parameters_for('/listPurchases')
        client_id = params.get('client_id')
        password = params.get('password')

        body = self._validate_parameter(client_id, 'Client ID')

        if body is not None:
            return Response(Response.BAD_REQUEST_RESPONSE, body)

        body = self._validate_parameter(password, 'Password')

        if body is not None:
            return Response(Response.BAD_REQUEST_RESPONSE, body)

        body = {'objects': self._system.list_purchases(client_id)}

        return Response(Response.OK_RESPONSE, body)

    def _validate_parameter(self, parameter, parameter_name):
        if parameter is None:
            return {'errors': f'1|{parameter_name} is missing'}
        return None
