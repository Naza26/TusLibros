class Cart:
    def __init__(self):
        self._books = []

    def is_empty(self):
        return len(self._books) == 0

    def add_book(self, book):
        self._books.append(book)

    def contains_book(self, book):
        return book in self._books
