class Cart:
    def __init__(self):
        self._catalogue = []

    def is_empty(self):
        return len(self._catalogue) == 0

    def add_book(self, book):
        self._catalogue.append(book)

    def contains_book(self, book):
        return book in self._catalogue

    def list_books(self):
        return self._catalogue
