from business.cart import Cart


class InternalCartSystem:
    def __init__(self):
        self.cart_system = {}
        #{'987': {
        #    'cart': Cart(),
        #    'client_info': {
        #        'client_id': '123',
        #        'password': 'password'
        #    }
        #}}

    def create_cart(self, client_id, password):
        self.validate_cart_creation_parameters(client_id, password)

        cart = Cart()
        cart_id = self._cart_id()
        self.cart_system[cart_id] = {'cart': cart, 'client_info': {'client_id': client_id, 'password': password}}

        return cart_id

    def _cart_id(self):
        return len(self.cart_system) + 1

    def validate_cart_creation_parameters(self, client_id, password):
        if client_id is None:
            raise ValueError('Client ID is missing')
        if password is None:
            raise ValueError('Password is missing')
