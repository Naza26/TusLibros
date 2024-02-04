import unittest

from system.internal_system import InternalCartSystem


class InternalTests(unittest.TestCase):

    def setUp(self):
        self.system = InternalCartSystem()

    def test_01_can_create_cart_when_client_id_and_password_are_provided(self):
        response = self.system.create_cart(self._a_client_id(), self._a_password())

        self.assertIsNotNone(response)

    def test_02_can_add_to_cart_if_all_required_parameters_are_provided(self):
        cart_id = self.system.create_cart(self._a_client_id(), self._a_password())

        response = self.system.add_to_cart(cart_id, self._a_book_isbn(), self._a_quantity_of_books())

        self._assert_books_were_successfully_added_to_cart(response, self._a_book_isbn())

    def test_03_can_list_cart_if_all_required_parameters_are_provided(self):
        cart_id = self.system.create_cart(self._a_client_id(), self._a_password())
        self.system.add_to_cart(cart_id, self._a_book_isbn(), self._a_quantity_of_books())

        response = self.system.list_cart(self._a_client_id())

        self._assert_listed_cart_contains_book_isbn_and_quantity(response)

    def test_04_cannot_add_books_when_cart_does_not_exist(self):
        non_existing_client_id = self._a_cart_id()

        self._assert_cannot_add_books_to_non_existing_cart(non_existing_client_id)

    def _assert_listed_cart_contains_book_isbn_and_quantity(self, response):
        self.assertEqual([f"{self._a_book_isbn()}|{1}"], response)

    def _assert_cannot_add_books_to_non_existing_cart(self, non_existing_cart_id):
        with self.assertRaises(ValueError) as context:
            self.system.add_to_cart(non_existing_cart_id, self._a_book_isbn(), self._a_quantity_of_books())
        self.assertEqual(str(context.exception), 'Cart does not exist')

    def _assert_books_were_successfully_added_to_cart(self, expected_response, expected_books):
        self.assertTrue(expected_response == self.system.SUCCESS_RESPONSE)
        listed_books = self.system.list_cart(1)
        self.assertTrue(expected_books, listed_books)

    def _a_client_id(self):
        return 'client_id'

    def _a_password(self):
        return 'password'

    def _a_book_isbn(self):
        return 'book_isbn'

    def _a_quantity_of_books(self):
        return 1

    def _a_cart_id(self):
        return 'cart_id'


if __name__ == '__main__':
    unittest.main()
