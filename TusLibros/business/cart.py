class Cart:
    def __init__(self):
        self.books = []

    def is_empty(self):
        return len(self.books) == 0

    def add_book(self, book):
        self.books.append(book)

    def contains_book(self, book):
        return book in self.books
