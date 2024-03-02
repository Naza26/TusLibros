import unittest

from http_protocol.requests.request import Request
from system.external_system import ExternalCartSystem


class ExternalTests(unittest.TestCase):

    def setUp(self):
        self.system = ExternalCartSystem()

    def test_01_cannot_create_cart_when_client_id_is_missing(self):
        request = Request()
        request.body.update({'client_id': None})

        response = self.system.create_cart(request)

        self.assertTrue(response.is_bad_request())
        self.assertTrue(response.failed_with_message("Client ID is missing"))

    def test_02_cannot_create_cart_when_password_is_missing(self):
        request = Request()
        request.body.update({'password': None})

        response = self.system.create_cart(request)

        self.assertTrue(response.is_bad_request())
        self.assertTrue(response.failed_with_message("Password is missing"))

    def test_03_can_create_cart_when_client_id_and_password_are_provided(self):
        request = Request()

        response = self.system.create_cart(request)

        self.assertIsNotNone(response.content())
        self.assertTrue(response.is_successful())

    def test_04_cannot_add_to_cart_if_cart_id_is_missing(self):
        request = Request()
        request.body.update({'cart_id': None})

        response = self.system.add_to_cart(request)

        self.assertTrue(response.is_bad_request())
        self.assertTrue(response.failed_with_message("Cart ID is missing"))

    def test_05_cannot_add_to_cart_if_client_id_is_missing(self):
        request = Request()
        request.body.update({'book_isbn': None})

        response = self.system.add_to_cart(request)

        self.assertTrue(response.is_bad_request())
        self.assertTrue(response.failed_with_message("Book ISBN is missing"))

    def test_06_cannot_add_to_cart_if_book_quantity_is_missing(self):
        request = Request()
        request.body.update({'book_quantity': None})

        response = self.system.add_to_cart(request)

        self.assertTrue(response.is_bad_request())
        self.assertTrue(response.failed_with_message("Book Quantity is missing"))

    def test_07_cannot_list_cart_if_client_id_is_missing(self):
        request = Request()
        request.body.update({'client_id': None})

        response = self.system.list_cart(request)

        self.assertTrue(response.is_bad_request())
        self.assertTrue(response.failed_with_message("Client ID is missing"))

    def _assert_parameter_is_required_for_cart_creation(self, request, parameter_name_to_validate):
        with self.assertRaises(ValueError) as context:
            self.system.create_cart(request)
        self.assertEqual(str(context.exception), f'{parameter_name_to_validate} is missing')

    def _assert_parameter_is_required_for_cart_addition(self, request, parameter_name_to_validate):
        with self.assertRaises(ValueError) as context:
            self.system.add_to_cart(request)
        self.assertEqual(str(context.exception), f'{parameter_name_to_validate} is missing')

    def _assert_parameter_is_required_for_cart_listing(self, request, parameter_name_to_validate):
        with self.assertRaises(ValueError) as context:
            self.system.list_cart(request)
        self.assertEqual(str(context.exception), f'{parameter_name_to_validate} is missing')

    def _assert_cannot_add_book_to_non_existing_cart(self, response):
        self.assertEqual(response, "Cart does not exist")


if __name__ == '__main__':
    unittest.main()
