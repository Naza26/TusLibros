import unittest

from system.internal_system import InternalCartSystem


# TODO: Doubt: Is it correct to save the call to some business logic in a variable named result instead of response?
# I was thinking in the internal face to call it result and in the outer face to call it response
# HTTP difference?
# TODO: Assert bussiness response in the external face or in the internal face?
class InternalTests(unittest.TestCase):

    def setUp(self):
        self.system = InternalCartSystem()

    def test_01_can_create_cart_when_credentials_are_provided(self):
        result = self.system.create_cart(self._a_client_id(), self._a_password())

        self._assert_is_valid_cart_id(result)

    def test_02_can_add_books_when_cart_is_created(self):
        cart_id = self.system.create_cart(self._a_client_id(), self._a_password())

        result = self.system.add_to_cart(cart_id, self._a_book_isbn(), self._a_quantity_of_books())

        self._assert_books_were_successfully_added_to_cart(result, self._a_book_isbn())

    def test_03_can_list_books_when_cart_is_created(self):
        cart_id = self.system.create_cart(self._a_client_id(), self._a_password())
        self.system.add_to_cart(cart_id, self._a_book_isbn(), self._a_quantity_of_books())

        result = self.system.list_cart(self._a_client_id())

        self._assert_listed_cart_contains_book_isbn_and_quantity(result)

    def test_04_cannot_add_books_when_cart_does_not_exist(self):
        non_existing_client_id = self._an_invalid_cart_id()

        self._assert_cannot_add_books_to_non_existing_cart(non_existing_client_id)

    def test_05_cannot_list_books_when_cart_does_not_exist(self):
        pass

    def _assert_listed_cart_contains_book_isbn_and_quantity(self, response):
        self.assertEqual([f"{self._a_book_isbn()}|{1}"], response)

    def _assert_cannot_add_books_to_non_existing_cart(self, non_existing_cart_id):
        with self.assertRaises(ValueError) as context:
            self.system.add_to_cart(non_existing_cart_id, self._a_book_isbn(), self._a_quantity_of_books())
        self.assertEqual(str(context.exception), 'Cart does not exist')

    def _assert_books_were_successfully_added_to_cart(self, expected_response, expected_books):
        # TODO: Check if below line should be verified in the external face since 200 is an HTTP status code
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

    def _an_invalid_cart_id(self):
        return 'cart_id'

    def _assert_is_valid_cart_id(self, result):
        try:
            int(result)
        except ValueError:
            self.fail("Cart ID is not valid")


if __name__ == '__main__':
    unittest.main()
