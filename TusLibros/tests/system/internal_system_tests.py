import unittest

from system.internal_system import InternalSystem


class InternalTests(unittest.TestCase):

    def setUp(self):
        self.system = InternalSystem()

    def test_01_can_create_cart_when_credentials_are_provided(self):
        cart_id = self.system.create_cart(self._a_client_id(), self._a_password())

        self._assert_is_valid(cart_id)

    def test_02_can_add_books_when_cart_is_created(self):
        cart_id = self.system.create_cart(self._a_client_id(), self._a_password())
        expected_books = [self._a_book()]

        result = self.system.add_to_cart(cart_id, self._a_book(), self._a_quantity_of_books())

        self._assert_books_were_successfully_added_to_cart(result, expected_books)

    def test_03_can_list_books_when_cart_is_created(self):
        cart_id = self.system.create_cart(self._a_client_id(), self._a_password())
        self.system.add_to_cart(cart_id, self._a_book(), self._a_quantity_of_books())

        result = self.system.list_cart(self._a_client_id())

        self._assert_listed_cart_contains_book_isbn_and_quantity(result)

    def test_04_cannot_add_books_when_cart_does_not_exist(self):
        non_existing_cart_id = self._an_invalid_cart_id()

        self._assert_cannot_add_books_to_non_existing_cart(non_existing_cart_id)

    def test_05_cannot_list_books_when_cart_does_not_exist(self):
        non_existing_cart_id = self._an_invalid_cart_id()

        self._assert_cannot_list_books_to_non_existing_cart(non_existing_cart_id)

    def _assert_listed_cart_contains_book_isbn_and_quantity(self, response):
        self.assertEqual([f"{self._a_book()}|{1}"], response)

    def _assert_cannot_add_books_to_non_existing_cart(self, non_existing_cart_id):
        with self.assertRaises(ValueError) as context:
            self.system.add_to_cart(non_existing_cart_id, self._a_book(), self._a_quantity_of_books())
        self.assertEqual(str(context.exception), 'Cart does not exist')

    def _assert_cannot_list_books_to_non_existing_cart(self, non_existing_cart_id):
        with self.assertRaises(ValueError) as context:
            self.system.list_cart(non_existing_cart_id)
        self.assertEqual(str(context.exception), 'Cart does not exist')

    def _assert_books_were_successfully_added_to_cart(self, expected_response, expected_books):
        listed_books = self.system.list_cart(1)
        self.assertTrue(expected_books, listed_books)

    def _a_client_id(self):
        return 'client_id'

    def _a_password(self):
        return 'password'

    # TODO: I should not be using this message to obtain a book here
    def _a_book(self):
        return 'Modern Software Engineering'

    def _a_quantity_of_books(self):
        return 1

    def _an_invalid_cart_id(self):
        return 'cart_id'

    def _assert_is_valid(self, cart_id):
        try:
            int(cart_id)
        except ValueError:
            self.fail("Cart ID is not valid")


if __name__ == '__main__':
    unittest.main()
