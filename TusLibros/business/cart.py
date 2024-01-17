class Cart:
    def __init__(self):
        self.books = []

    def is_empty(self):
        return len(self.books) == 0
