from http_protocol.response import Response
from system.internal_system import InternalSystem


class ExternalSystem:
    def __init__(self):
        self._system = InternalSystem()

    def create_cart(self, request):
        params = request.http_post_parameters_for('/createCart')

        body = self._build_body_with(self._system.create_cart, **params)

        if 'errors' in body:
            return Response(Response.BAD_REQUEST_RESPONSE, body)
        else:
            return Response(Response.OK_RESPONSE, body)

    def add_to_cart(self, request):
        params = request.http_post_parameters_for('/addToCart')
        body = self._build_body_with(self._system.add_to_cart, **params)

        if 'errors' in body:
            return Response(Response.BAD_REQUEST_RESPONSE, body)
        else:
            return Response(Response.OK_RESPONSE, body)

    def list_cart(self, request):
        params = request.http_post_parameters_for('/listCart')

        body = self._build_body_with(self._system.list_cart, **params)

        if 'errors' in body:
            return Response(Response.BAD_REQUEST_RESPONSE, body)
        else:
            return Response(Response.OK_RESPONSE, body)

    def checkout_cart(self, request):
        params = request.http_post_parameters_for('/checkoutCart')
        body = self._build_body_with(self._system.checkout_cart, **params)

        if 'errors' in body:
            return Response(Response.BAD_REQUEST_RESPONSE, body)
        else:
            return Response(Response.OK_RESPONSE, body)

    def list_purchases(self, request):
        params = request.http_post_parameters_for('/listPurchases')
        body = self._build_body_with(self._system.list_purchases, **params)

        if 'errors' in body:
            return Response(Response.BAD_REQUEST_RESPONSE, body)
        else:
            return Response(Response.OK_RESPONSE, body)

    def _validate_parameter(self, parameter, parameter_name):
        if parameter is None:
            return {'errors': f'1|{parameter_name} is missing'}
        return None

    def _build_body_with(self, url_resource, **params):
        for parameter_name, parameter_value in params.items():
            if parameter_value is None:
                return {'errors': f'1|{parameter_name} is missing'}

        return {'objects': url_resource(**params)}
