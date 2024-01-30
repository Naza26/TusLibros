class Cart:
    def __init__(self):
        self._items = []

    def is_empty(self):
        return len(self._items) == 0

    def add_book(self, book):
        self._items.append(book)

    def contains_book(self, book):
        return book in self._items

    def list_books(self):
        return self._items
