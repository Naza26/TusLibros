from business.cart import Cart
from business.catalogue import Catalogue


class InternalSystem:
    SUCCESS_RESPONSE = "OK"

    def __init__(self):
        # TODO: Ask if this is not breaking the heuristic of creating complete and valid objects
        # SOLVED: This is fine for now. I will need to refactor it later on when I have multiple carts.
        self._cart = None

    def create_cart(self, client_id, password):
        # I would want to validate that the client id can be parsed and something with the password

        self._cart = Cart(Catalogue(self._books_in_stock()))

        return 1

    def add_to_cart(self, cart_id, book_isbn, book_quantity):
        # I would want to validate that the cart id can be parsed and that the book quantity is a number
        self._validate_cart_exists()

        self._cart.add_book(book_isbn)

        return self.SUCCESS_RESPONSE

    def list_cart(self, client_id):
        # I would want to validate that the client id can be parsed
        self._validate_cart_exists()

        books = self._cart.list_books()

        return self._present_books(books)

    def checkout_cart(self, cart_id, credit_card_number, credit_card_expiration_date, credit_card_owner):
        # I would want to validate that the cart id can be parsed and that the credit card number is a number
        self._validate_cart_exists()

        self._cart.checkout(cart_id, credit_card_number, credit_card_expiration_date, credit_card_owner)

        return self.SUCCESS_RESPONSE

    def list_purchases(self, client_id):
        # I would want to validate that the client id can be parsed
        self._validate_cart_exists()

        purchases = self._cart.list_purchases(client_id)

        return self._present_purchases(purchases)

    def _validate_cart_exists(self):
        if self._cart is None:
            raise ValueError("Cart does not exist")

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

    def _books_in_stock(self):
        return [
            'Modern Software Engineering',
            'Extreme Programming Explained'
            'Planning Extreme Programming',
            'Domain-Driven Design',
            'Object Thinking',
            'Test Driven Development: By Example'
        ]
