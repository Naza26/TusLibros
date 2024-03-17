from flask import Flask


class WebServer:
    DEFAULT_PORT_NUMBER = 5000

    def __init__(self):
        self._port_number = self.DEFAULT_PORT_NUMBER
        self._app = Flask(__name__)

        self.register_routes()

    def application(self):
        return self._app

    def run_with_configuration(self, host, debug, port=DEFAULT_PORT_NUMBER):
        self._app.run(host=host, port=port, debug=debug)

    def register_routes(self):
        @self._app.route('/')
        def index():
            return 'Index Page'

        @self._app.route('/hello')
        def hello():
            return 'Hello, World'

        @self._app.route('/createCart')
        def create_cart():
            return 'Hello, CART'


web_server = WebServer()

if __name__ == '__main__':
    web_server.run_with_configuration(host="localhost", debug=True, port=8000)
