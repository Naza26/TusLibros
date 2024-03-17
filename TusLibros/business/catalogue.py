from business.editorial_system import EditorialSystem


class Catalogue:
    def __init__(self, books=EditorialSystem.books_in_stock()):
        self._books = books

    def is_book_in_catalogue(self, book):
        return book in self._books

    def a_book(self):
        return self._books[0]

    def another_book(self):
        return self._books[-1]
