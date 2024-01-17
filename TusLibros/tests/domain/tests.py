import unittest

from business.cart import Cart


class DomainTest(unittest.TestCase):
    def test_a_cart_with_no_books_is_empty(self):
        cart = Cart()

        self.assertTrue(cart.is_empty())

    def test_a_cart_with_books_is_not_empty(self):
        cart = Cart()

        cart.add_book('Modern Software Engineering')

        self.assertFalse(cart.is_empty())

    def test_the_cart_contains_the_added_book(self):
        cart = Cart()

        cart.add_book('Modern Software Engineering')

        self.assertTrue(cart.contains_book('Modern Software Engineering'))


if __name__ == '__main__':
    unittest.main()
