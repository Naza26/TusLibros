from business.catalogue import Catalogue


class EditorialSystem:

    def __init__(self, cart, new_catalogue):
        self._catalogue = Catalogue(new_catalogue or self._books_in_stock())
        self._cart = cart

    def catalogue(self):
        return self._catalogue

    def cart(self):
        return self._cart

    def _books_in_stock(self):
        return [
            'Modern Software Engineering',
            'Extreme Programming Explained'
            'Planning Extreme Programming',
            'Domain-Driven Design',
            'Object Thinking',
            'Test Driven Development: By Example'
        ]
