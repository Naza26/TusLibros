from business.catalogue import Catalogue


class Cart:
    def __init__(self):
        self._items = []
        # TODO: I don't think the cart should know about the catalogue. I need to understand how to relation the 3 entities.
        self._catalogue = Catalogue(self._books_in_stock())

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

    # TODO: This message should not go here, it's supposed to be in the editorial
    def _books_in_stock(self):
        return [
            'Modern Software Engineering',
            'Extreme Programming Explained'
            'Planning Extreme Programming',
            'Domain-Driven Design',
            'Object Thinking',
            'Test Driven Development: By Example'
        ]