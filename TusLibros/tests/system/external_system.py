import unittest

from http_protocol.requests.create_cart_request import CreateCartRequest
from system.external_system import ExternalCartSystem


class ExternalTests(unittest.TestCase):

    def setUp(self):
        self.system = ExternalCartSystem()
        self.request = None

    def test_01_cannot_create_cart_when_client_id_is_missing(self):
        self.request = CreateCartRequest()
        client_id = None

        self._assert_parameter_is_required_for_cart_creation(client_id, self._a_password(), "Client ID")

    def test_02_cannot_create_cart_when_password_is_missing(self):
        password = None

        self._assert_parameter_is_required_for_cart_creation(self._a_client_id(), password, "Password")

    def test_03_cannot_add_to_cart_if_cart_id_is_missing(self):
        cart_id = None

        self._assert_parameter_is_required_for_cart_addition(cart_id, self._a_book_isbn(), self._a_quantity_of_books(),
                                                             "Cart ID")

    def test_04_cannot_add_to_cart_if_client_id_is_missing(self):
        book_isbn = None

        self._assert_parameter_is_required_for_cart_addition(self._a_cart_id(), book_isbn, self._a_quantity_of_books(),
                                                             "Book ISBN")

    def test_05_cannot_add_to_cart_if_book_quantity_is_missing(self):
        book_quantity = None

        self._assert_parameter_is_required_for_cart_addition(self._a_cart_id(), self._a_book_isbn(), book_quantity,
                                                             "Book Quantity")

    def test_06_cannot_list_cart_if_client_id_is_missing(self):
        client_id = None

        self._assert_parameter_is_required_for_cart_listing(client_id, "Client ID")

    def _assert_cannot_add_book_to_non_existing_cart(self, response):
        self.assertEqual(response, "Cart does not exist")

    def _assert_parameter_is_required_for_cart_creation(self, client_id, password, parameter_name_to_validate):
        with self.assertRaises(ValueError) as context:
            self.system.create_cart(client_id, password)
        self.assertEqual(str(context.exception), f'{parameter_name_to_validate} is missing')

    def _assert_parameter_is_required_for_cart_addition(self, cart_id, book_isbn, quantity_of_books,
                                                        parameter_name_to_validate):
        with self.assertRaises(ValueError) as context:
            self.system.add_to_cart(cart_id, book_isbn, quantity_of_books)
        self.assertEqual(str(context.exception), f'{parameter_name_to_validate} is missing')

    def _assert_parameter_is_required_for_cart_listing(self, client_id, parameter_name_to_validate):
        with self.assertRaises(ValueError) as context:
            self.system.list_cart(client_id)
        self.assertEqual(str(context.exception), f'{parameter_name_to_validate} is missing')

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
