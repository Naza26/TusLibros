def default_books():
    return [
        'Modern Software Engineering',
        'Extreme Programming Explained'
        'Planning Extreme Programming',
        'Domain-Driven Design',
        'Object Thinking',
        'Test Driven Development: By Example'
    ]


class Catalogue:
    DEFAULT_QUANTITY = 1

    def __init__(self, books=default_books()):
        self._books = books

    @classmethod
    def book_is_not_in_catalogue_error_message(cls):
        return 'Book is not in catalogue'

    def is_book_in_catalogue(self, book):
        return book in self._books

    def a_book(self):
        return self._books[0]

    def another_book(self):
        return self._books[-1]

    def a_book_that_is_not_in_catalogue(self):
        return 'Cormen'
