from business.catalogue import Catalogue


class Cart:
    def __init__(self, catalogue):
        self._items = []
        # TODO: Understand how to decouple the catalogue from the cart.
        self._catalogue = catalogue

    def is_empty(self):
        return len(self._items) == 0

    def add_book(self, book):
        if not self._catalogue.is_book_in_catalogue(book):
            raise ValueError('Book is not in catalogue')
        self._items.append(book)

    def contains_book(self, book):
        return book in self._items

    def list_books(self):
        return self._items.copy()

    def checkout(self, cart_id, credit_card_number, credit_card_expiration_date, credit_card_owner):
        return 1

    def list_purchases(self, client_id, password):
        return []
