from business.cart import Cart
from business.catalogue import Catalogue


class InternalSystem:
    SUCCESS_RESPONSE = "OK"
    ERROR_RESPONSE = "ERROR"

    'initialization'

    def __init__(self):
        self._carts = {}

    'public'

    def create_cart(self, client_id, password):
        # Validate credentials against some service?
        new_cart = Cart(Catalogue())
        cart_id = self._generate_new_cart_id()
        self._register_new_cart_given(cart_id, new_cart)

        return cart_id

    def add_to_cart(self, cart_id, book_isbn, book_quantity):
        # I would want to validate that the cart id can be parsed and that the book quantity is a number
        self._validate_cart_exists_given(cart_id)
        cart = self._carts[cart_id]

        try:
            cart.add_book(book_isbn)
            return self.SUCCESS_RESPONSE
        except ValueError:
            self.ERROR_RESPONSE

    def list_cart(self, cart_id):
        # I would want to validate that the cart id can be parsed
        self._validate_cart_exists_given(cart_id)
        cart = self._carts[cart_id]

        books = cart.list_books()

        return self._present_books(books)

    def checkout_cart(self, cart_id, credit_card_number, credit_card_expiration_date, credit_card_owner):
        # I would want to validate that the cart id can be parsed and that the credit card number is a number
        self._validate_cart_exists_given(cart_id)
        cart = self._carts[cart_id]

        cart.checkout(cart_id, credit_card_number, credit_card_expiration_date, credit_card_owner)

        return self.SUCCESS_RESPONSE

    def list_purchases(self, client_id, password):
        # I would want to validate that the client id can be parsed
        self._validate_cart_exists_given(client_id)
        cart = self._carts[client_id]

        purchases = cart.list_purchases(client_id, password)

        return self._present_purchases(purchases)

    'private'

    def _register_new_cart_given(self, cart_id, new_cart):
        self._carts[cart_id] = new_cart

    def _generate_new_cart_id(self):
        return len(self._carts) + 1

    def _validate_cart_exists_given(self, cart_id):
        if cart_id not in self._carts:
            raise ValueError('Cart does not exist')

    def _present_books(self, books):
        books_to_list = []

        for book in books:
            books_to_list.append(f"{book}|{1}")

        return books_to_list

    def _present_purchases(self, purchases):
        purchases_to_list = []

        for purchase in purchases:
            purchases_to_list.append(f"{'ISBN'}|{1}")

        return purchases_to_list
