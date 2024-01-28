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
        if client_id is None:
            return 'Client ID is missing'
        if password is None:
            return 'Password is missing'
        cart = Cart()
        cart_id = len(self.cart_system) + 1
        self.cart_system[cart_id] = {'cart': cart, 'client_info': {'client_id': client_id, 'password': password}}
        return cart_id
