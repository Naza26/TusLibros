import unittest

from http_protocol.requests.create_cart_request import CreateCartRequest
from system.external_system import ExternalCartSystem


class ExternalTests(unittest.TestCase):

    def setUp(self):
        self.system = ExternalCartSystem()
        self.request = None

    # TODO: Ask if modelling a request for each endpoint makes sense. IDK if it's a lot of overhead
    # I wanted to put in that object what each enpoint was expecting as required parameters
    def test_01_cannot_create_cart_when_client_id_is_missing(self):
        self.request = CreateCartRequest()
        client_id = None
        password = self._get_password_from(self.request)

        self._assert_parameter_is_required_for_cart_creation(client_id, password, "Client ID")

    def test_02_cannot_create_cart_when_password_is_missing(self):
        client_id = self._get_client_id_from(self.request)
        password = None

        self._assert_parameter_is_required_for_cart_creation(client_id, password, "Password")

    def test_03_can_create_cart_when_client_id_and_password_are_provided(self):
        client_id = self._get_client_id_from(self.request)
        password = self._get_password_from(self.request)

        response = self.system.create_cart(client_id, password)

        self.assertIsNotNone(response)

    def test_04_cannot_add_to_cart_if_cart_id_is_missing(self):
        cart_id = None
        book_isbn = self._get_book_isbn_from(self.request)
        book_quantity = self._get_quantity_of_books_from(self.request)

        self._assert_parameter_is_required_for_cart_addition(cart_id, book_isbn, book_quantity, "Cart ID")

    def test_05_cannot_add_to_cart_if_client_id_is_missing(self):
        client_id = self._get_cart_id_from(self.request)
        book_isbn = None
        book_quantity = self._get_quantity_of_books_from(self.request)

        self._assert_parameter_is_required_for_cart_addition(client_id, book_isbn, book_quantity, "Book ISBN")

    def test_06_cannot_add_to_cart_if_book_quantity_is_missing(self):
        cart_id = self._get_cart_id_from(self.request)
        book_isbn = self._get_book_isbn_from(self.request)
        book_quantity = None

        self._assert_parameter_is_required_for_cart_addition(cart_id, book_isbn, book_quantity, "Book Quantity")

    def test_07_cannot_list_cart_if_client_id_is_missing(self):
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

    def _get_client_id_from(self, request):
        return 'client_id'

    def _get_password_from(self, request):
        return 'password'

    def _get_book_isbn_from(self, request):
        return 'book_isbn'

    def _get_quantity_of_books_from(self, request):
        return 1

    def _get_cart_id_from(self, request):
        return 'cart_id'


if __name__ == '__main__':
    unittest.main()
