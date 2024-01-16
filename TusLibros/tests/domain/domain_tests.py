import unittest

from business.cart import Cart


class DomainTests(unittest.TestCase):
    def a_cart_with_no_books_is_empty(self):
        cart = Cart()
        self.assertTrue(cart.is_empty())


if __name__ == '__main__':
    unittest.main()
