import unittest

from business.cart import Cart
from business.catalogue import Catalogue


class CartTests(unittest.TestCase):

    def setUp(self):
        self._catalogue = Catalogue()
        self._cart = Cart(self._catalogue)

    def test_01_a_cart_with_no_books_is_empty(self):
        self.assertTrue(self._cart.is_empty())

    def test_02_a_cart_with_books_is_not_empty(self):
        self._cart.add_book(self._a_book())

        self.assertFalse(self._cart.is_empty())

    def test_03_the_cart_contains_the_added_book(self):
        self._cart.add_book(self._a_book())

        self.assertTrue(self._cart.contains_book(self._a_book()))

    def test_04_the_cart_does_not_contain_a_book_not_added(self):
        self._cart.add_book(self._a_book())

        self.assertFalse(self._cart.contains_book(self._another_book()))

    def test_05_books_added_to_the_cart_can_be_listed(self):
        self._cart.add_book(self._a_book())
        self._cart.add_book(self._another_book())

        listed_books = self._cart.list_books()

        self.assertEqual([self._a_book(), self._another_book()], listed_books)

    def test_06_cannot_add_book_that_is_not_in_catalogue(self):
        self._assert_cannot_add_book_that_is_not_in_catalogue(self._cart)

    def test_07_can_add_books_in_multiple_carts(self):
        another_cart = Cart(self._catalogue)

        self._cart.add_book(self._a_book())
        another_cart.add_book(self._another_book())

        self.assertTrue(self._cart.contains_book(self._a_book()))
        self.assertTrue(another_cart.contains_book(self._another_book()))

    def _assert_cannot_add_book_that_is_not_in_catalogue(self, cart):
        with self.assertRaises(ValueError) as context:
            cart.add_book(self._a_book_that_is_not_in_catalogue())
        self.assertEqual(str(context.exception), 'Book is not in catalogue')

    def _a_book(self):
        return self._catalogue.a_book()

    def _another_book(self):
        return self._catalogue.another_book()

    def _a_book_that_is_not_in_catalogue(self):
        return 'Cormen'


if __name__ == '__main__':
    unittest.main()
