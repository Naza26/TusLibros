import unittest

from http_protocol.request import Request
from system.external_system import ExternalSystem


class ExternalSystemFactory:

    def __init__(self):
        self.external_system = ExternalSystem()

    def system(self):
        return self.external_system

    def create_body_with_empty_client_id(self):
        return {'client_id': None, 'password': 'password'}

    def create_body_with_empty_password(self):
        return {'client_id': 'client_id', 'password': None}

    def create_body_with_valid_credentials(self):
        return {'client_id': 'client_id', 'password': 'password'}

    def create_body_with_empty_cart_id(self):
        return {'cart_id': None, 'book_isbn': 'Modern Software Engineering', 'book_quantity': 2}

    def create_body_with_empty_book_isbn(self):
        return {'cart_id': 'cart_id', 'book_isbn': None, 'book_quantity': 2}

    def create_body_with_empty_book_quantity(self):
        return {'cart_id': 'cart_id', 'book_isbn': 'Modern Software Engineering', 'book_quantity': None}

    def create_body_with_valid_cart_id(self):
        return {'cart_id': 'cart_id', 'book_isbn': 'Modern Software Engineering', 'book_quantity': 2}


class ExternalSystemTests(unittest.TestCase):

    def setUp(self):
        self.external_system_factory = ExternalSystemFactory()
        self.system = self.external_system_factory.system()

    def test_01_cannot_create_cart_when_client_id_is_missing(self):
        body = self.external_system_factory.create_body_with_empty_client_id()
        request = Request(Request.HTTP_POST_METHOD, '/createCart', body)

        response = self.system.create_cart(request)

        self.assertTrue(response.is_bad_request())
        self.assertTrue(response.failed_with_message("client_id is missing"))

    def test_02_cannot_create_cart_when_password_is_missing(self):
        body = self.external_system_factory.create_body_with_empty_password()
        request = Request(Request.HTTP_POST_METHOD, '/createCart', body)

        response = self.system.create_cart(request)

        self.assertTrue(response.is_bad_request())
        self.assertTrue(response.failed_with_message("password is missing"))

    def test_03_can_create_cart_when_client_id_and_password_are_provided(self):
        body = self.external_system_factory.create_body_with_valid_credentials()
        request = Request(Request.HTTP_POST_METHOD, '/createCart', body)

        response = self.system.create_cart(request)

        self.assertIsNotNone(response.content())
        self.assertTrue(response.is_successful())

    def test_04_cannot_add_to_cart_if_cart_id_is_missing(self):
        body = self.external_system_factory.create_body_with_empty_cart_id()
        request = Request(Request.HTTP_POST_METHOD, '/addToCart', body)

        response = self.system.add_to_cart(request)

        self.assertTrue(response.is_bad_request())
        self.assertTrue(response.failed_with_message("cart_id is missing"))

    def test_05_cannot_add_to_cart_if_book_isbn_is_missing(self):
        body = self.external_system_factory.create_body_with_empty_book_isbn()
        request = Request(Request.HTTP_POST_METHOD, '/addToCart', body)

        response = self.system.add_to_cart(request)

        self.assertTrue(response.is_bad_request())
        self.assertTrue(response.failed_with_message("book_isbn is missing"))

    def test_06_cannot_add_to_cart_if_book_quantity_is_missing(self):
        body = self.external_system_factory.create_body_with_empty_book_quantity()
        request = Request(Request.HTTP_POST_METHOD, '/addToCart', body)

        response = self.system.add_to_cart(request)

        self.assertTrue(response.is_bad_request())
        self.assertTrue(response.failed_with_message("book_quantity is missing"))

    def test_07_can_add_books_when_cart_exists(self):
        body = {'client_id': 'client_id', 'password': 'password'}
        request = Request(Request.HTTP_POST_METHOD, '/createCart', body)
        self.system.create_cart(request)
        body = {'cart_id': 'cart_id', 'book_isbn': 'Modern Software Engineering', 'book_quantity': 2}
        request = Request(Request.HTTP_POST_METHOD, '/addToCart', body)

        response = self.system.add_to_cart(request)

        self.assertTrue(response.is_successful())

    def test_08_cannot_list_cart_if_cart_id_is_missing(self):
        body = {'cart_id': None}
        request = Request(Request.HTTP_GET_METHOD, '/listCart', body)

        response = self.system.list_cart(request)

        self.assertTrue(response.is_bad_request())
        self.assertTrue(response.failed_with_message("cart_id is missing"))

    def test_09_can_list_books_when_cart_exists(self):
        body = {'client_id': 'client_id', 'password': 'password'}
        request = Request(Request.HTTP_GET_METHOD, '/createCart', body)
        self.system.create_cart(request)

        body = {'cart_id': 'cart_id', 'book_isbn': 'Modern Software Engineering', 'book_quantity': 2}
        request = Request(Request.HTTP_POST_METHOD, '/addToCart', body)
        self.system.add_to_cart(request)

        body = {'cart_id': 'cart_id'}
        request = Request(Request.HTTP_POST_METHOD, '/listCart', body)

        response = self.system.list_cart(request)

        self.assertTrue(response.is_successful())
        self.assertIsNotNone(response.content())

    def test_10_cannot_checkout_cart_if_cart_id_is_missing(self):
        body = {'cart_id': None,
                'credit_card_number': '1234567890',
                'credit_card_expiration_date': '399',
                'credit_card_owner': 'John Doe'}
        request = Request(Request.HTTP_POST_METHOD, '/checkoutCart', body)

        response = self.system.checkout_cart(request)

        self.assertTrue(response.is_bad_request())
        self.assertTrue(response.failed_with_message("cart_id is missing"))

    def test_11_cannot_checkout_cart_if_credit_card_number_is_missing(self):
        body = {'cart_id': 'cart_id',
                'credit_card_number': None,
                'credit_card_expiration_date': '399',
                'credit_card_owner': 'John Doe'}
        request = Request(Request.HTTP_POST_METHOD, '/checkoutCart', body)

        response = self.system.checkout_cart(request)

        self.assertTrue(response.is_bad_request())
        self.assertTrue(response.failed_with_message("credit_card_number is missing"))

    def test_12_cannot_checkout_cart_if_credit_card_expiration_date_is_missing(self):
        body = {'cart_id': 'cart_id',
                'credit_card_number': '1234567890',
                'credit_card_expiration_date': None,
                'credit_card_owner': 'John Doe'}
        request = Request(Request.HTTP_POST_METHOD, '/checkoutCart', body)

        response = self.system.checkout_cart(request)

        self.assertTrue(response.is_bad_request())
        self.assertTrue(response.failed_with_message("credit_card_expiration_date is missing"))

    def test_13_cannot_checkout_cart_if_credit_card_owner_is_missing(self):
        body = {'cart_id': 'cart_id',
                'credit_card_number': '1234567890',
                'credit_card_expiration_date': '399',
                'credit_card_owner': None}
        request = Request(Request.HTTP_POST_METHOD, '/checkoutCart', body)

        response = self.system.checkout_cart(request)

        self.assertTrue(response.is_bad_request())
        self.assertTrue(response.failed_with_message("credit_card_owner is missing"))

    def test_14_can_checkout_cart_when_all_parameters_are_provided(self):
        body = {'client_id': 'client_id', 'password': 'password'}
        request = Request(Request.HTTP_POST_METHOD, '/createCart', body)
        self.system.create_cart(request)

        body = {'cart_id': 'cart_id', 'book_isbn': 'Modern Software Engineering', 'book_quantity': 2}
        request = Request(Request.HTTP_POST_METHOD, '/addToCart', body)
        self.system.add_to_cart(request)

        body = {'cart_id': 'cart_id',
                'credit_card_number': '1234567890',
                'credit_card_expiration_date': '399',
                'credit_card_owner': 'John Doe'}
        request = Request(Request.HTTP_POST_METHOD, '/checkoutCart', body)

        response = self.system.checkout_cart(request)

        self.assertTrue(response.is_successful())

    def test_15_cannot_list_purchases_if_client_id_is_missing(self):
        body = {'client_id': None, 'password': 'password'}
        request = Request(Request.HTTP_GET_METHOD, 'listPurchases', body)

        response = self.system.list_purchases(request)

        self.assertTrue(response.is_bad_request())
        self.assertTrue(response.failed_with_message("client_id is missing"))

    def test_16_cannot_list_purchases_if_password_is_missing(self):
        body = {'client_id': 'client_id', 'password': None}
        request = Request(Request.HTTP_GET_METHOD, 'listPurchases', body)

        response = self.system.list_purchases(request)

        self.assertTrue(response.is_bad_request())
        self.assertTrue(response.failed_with_message("password is missing"))

    def test_17_can_list_purchases_when_credentials_are_provided(self):
        body = {'client_id': 'client_id', 'password': 'password'}
        request = Request(Request.HTTP_POST_METHOD, '/createCart', body)
        self.system.create_cart(request)

        body = {'cart_id': 'cart_id', 'book_isbn': 'Modern Software Engineering', 'book_quantity': 2}
        request = Request(Request.HTTP_POST_METHOD, '/addToCart', body)
        self.system.add_to_cart(request)

        body = {'cart_id': 'cart_id',
                'credit_card_number': '1234567890',
                'credit_card_expiration_date': '399',
                'credit_card_owner': 'John Doe'}
        request = Request(Request.HTTP_POST_METHOD, '/checkoutCart', body)
        self.system.checkout_cart(request)

        body = {'client_id': 'client_id', 'password': 'password'}
        request = Request(Request.HTTP_GET_METHOD, 'listPurchases', body)

        response = self.system.list_purchases(request)

        self.assertTrue(response.is_successful())
        self.assertIsNotNone(response.content())


if __name__ == '__main__':
    unittest.main()
