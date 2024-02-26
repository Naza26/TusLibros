class Request:
    def __init__(self):
        self.http_method = 'GET'
        self.url = None
        self.body = {'client_id': 'client_id', 'password': 'password', 'cart_id': 'cart_id', 'book_isbn': 'book_isbn',
                     'book_quantity': 2}

    def http_get_parameters(self):
        return 1

    def http_post_parameters_for(self, url):
        if '/createCart' in url:
            self.body.update({'client_id': self._client_id(), 'password': self._password()})
        if '/addToCart' in url:
            self.body.update({'cart_id': None, 'book_isbn': None, 'book_quantity': None})

        return self.body

    def _client_id(self):
        return "client_id"

    def _password(self):
        return "password"
