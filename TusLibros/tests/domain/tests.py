import unittest

from business.cart import Cart


class DomainTest(unittest.TestCase):
    def test_a_cart_with_no_books_is_empty(self):
        cart = Cart()

        self.assertTrue(cart.is_empty())

    def test_a_cart_with_books_is_not_empty(self):
        cart = Cart()

        cart.add_book(self._a_book())

        self.assertFalse(cart.is_empty())

    def _a_book(self):
        return 'Modern Software Engineering'

    def test_the_cart_contains_the_added_book(self):
        cart = Cart()

        cart.add_book(self._a_book())

        self.assertTrue(cart.contains_book(self._a_book()))

    def test_the_cart_does_not_contain_a_book_not_added(self):
        cart = Cart()

        cart.add_book(self._a_book())

        self.assertFalse(cart.contains_book(self._another_book()))

    def _another_book(self):
        return 'Extreme Programming Explained'


if __name__ == '__main__':
    unittest.main()
