from flask import Flask, request, Response

from http_protocol.request import Request
from http_protocol.response import Response
from system.external_system import ExternalSystem


class WebServer:
    DEFAULT_PORT_NUMBER = 5000

    def __init__(self):
        self._app = Flask(__name__)
        self._port_number = self.DEFAULT_PORT_NUMBER
        self._rest_interface = ExternalSystem()

        self._register_endpoints()

    def run_with_configuration(self, host, debug, port=DEFAULT_PORT_NUMBER):
        self._app.run(host=host, port=port, debug=debug)

    def _register_endpoints(self):
        @self._app.route('/createCart')
        def create_cart():
            return self._execute_resource_for('create_cart')

        @self._app.route('/addToCart')
        def add_to_cart():
            return self._execute_resource_for('add_to_cart')

        @self._app.route('/listCart')
        def list_cart():
            return self._execute_resource_for('list_cart')

        @self._app.route('/checkOutCart')
        def checkout_cart():
            return self._execute_resource_for('checkout_cart')

        @self._app.route('/listPurchases')
        def list_purchases():
            return self._execute_resource_for('list_purchases')

    def _execute_resource_for(self, endpoint):
        http_request = Request(request.method, endpoint, request.args.to_dict())
        execute_resource_for = self._rest_interface_resource_from(endpoint)
        http_response = execute_resource_for(http_request)
        return Response(http_response.content(), str(http_response.status_code()))

    def _rest_interface_resource_from(self, endpoint):
        return getattr(self._rest_interface, endpoint)


if __name__ == '__main__':
    web_server = WebServer()
    web_server.run_with_configuration(host="localhost", debug=True, port=8000)
