class Catalogue:
    def __init__(self, books):
        self.books = books

    def is_book_in_catalogue(self, book):
        return book in self.books