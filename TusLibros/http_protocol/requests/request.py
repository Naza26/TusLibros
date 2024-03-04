class Request:
    def __init__(self):
        self.http_method = 'GET'
        self.url = None
        self.body = {'client_id': 'client_id', 'password': 'password', 'cart_id': 'cart_id',
                     'book_isbn': 'Modern Software Engineering', 'book_quantity': 2,
                     'credit_card_number': '1234567890', 'credit_card_expiration_date': '399',
                     'credit_card_owner': 'John Doe'}

    def http_get_parameters(self):
        return 1

    def http_post_parameters_for(self, url):
        if '/createCart' in url:
            body_items = list(self.body.items())
            body_items = body_items[:2]
            return dict(body_items)
        if '/addToCart' in url:
            body_items = list(self.body.items())
            body_items = body_items[1:]
            return dict(body_items)
        if '/listCart' in url:
            body_items = list(self.body.items())
            body_items = body_items[:1]
            return dict(body_items)
        if '/checkoutCart' in url:
            body_items = list(self.body.items())
            return dict(body_items)

        return self.body

    def _client_id(self):
        return "client_id"

    def _password(self):
        return "password"
