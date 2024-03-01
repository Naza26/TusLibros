from business.cart import Cart
from tests.business.catalogue import Catalogue


class Editorial:

    def __init__(self):
        self._catalogue = Catalogue(self.books_in_stock())
        self._cart = Cart()

    def books_in_stock(self):
        return [
            'Modern Software Engineering',
            'Extreme Programming Explained'
        ]

    def catalogue(self):
        return self._catalogue

    def cart(self):
        return self._cart