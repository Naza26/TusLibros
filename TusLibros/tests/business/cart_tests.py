import unittest

from business.cart import Cart
from business.editorial import Editorial


class CartTests(unittest.TestCase):

    def setUp(self):
        self._editorial = Editorial(Cart())
        self._catalogue = self._editorial.catalogue()

    def test_a_cart_with_no_books_is_empty(self):
        cart = self._editorial.cart()

        self.assertTrue(cart.is_empty())

    def test_a_cart_with_books_is_not_empty(self):
        cart = self._editorial.cart()

        cart.add_book(self._a_book())

        self.assertFalse(cart.is_empty())

    def test_the_cart_contains_the_added_book(self):
        cart = self._editorial.cart()

        cart.add_book(self._a_book())

        self.assertTrue(cart.contains_book(self._a_book()))

    def test_the_cart_does_not_contain_a_book_not_added(self):
        cart = self._editorial.cart()

        cart.add_book(self._a_book())

        self.assertFalse(cart.contains_book(self._another_book()))

    def test_books_added_to_the_cart_can_be_listed(self):
        cart = self._editorial.cart()
        cart.add_book(self._a_book())
        cart.add_book(self._another_book())

        listed_books = cart.list_books()

        self.assertEqual([self._a_book(), self._another_book()], listed_books)

    def test_cannot_add_book_that_is_not_in_catalogue(self):
        cart = self._editorial.cart()
        with self.assertRaises(ValueError) as context:
            cart.add_book('Non existent book')
        self.assertEqual(str(context.exception), 'Book is not in catalogue')

    def _a_book(self):
        return self._editorial.catalogue().a_book()

    def _another_book(self):
        return self._editorial.catalogue().another_book()


if __name__ == '__main__':
    unittest.main()
