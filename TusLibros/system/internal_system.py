from business.cart import Cart


class InternalCartSystem:
    SUCCESS_RESPONSE = "OK"

    def __init__(self):
        # TODO: Ask if this is not breaking the heuristic of creating complete and valid objects
        self._cart = None

    def create_cart(self, client_id, password):
        # I would want to validate that the client id can be parsed and something with the password

        self._cart = Cart()

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

    def _validate_cart_exists(self):
        if self._cart is None:
            raise ValueError("Cart does not exist")

    def _present_books(self, books):
        books_to_list = []

        for book in books:
            books_to_list.append(f"{book}|{1}")

        return books_to_list

    def cart_exists_with(self, cart_id):
        return self._cart is not None
