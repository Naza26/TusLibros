class EditorialSystem:

    def __init__(self, cart, new_catalogue):
        # self._catalogue = Catalogue(new_catalogue)
        self._cart = cart


    @classmethod
    def books_in_stock(cls):
        return [
            'Modern Software Engineering',
            'Extreme Programming Explained'
            'Planning Extreme Programming',
            'Domain-Driven Design',
            'Object Thinking',
            'Test Driven Development: By Example'
        ]

    def catalogue(self):
        return self._catalogue

    def cart(self):
        return self._cart

