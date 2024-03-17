import unittest

from http_protocol.request import Request
from system.external_system import ExternalSystem


class ExternalTests(unittest.TestCase):

    def setUp(self):
        self.system = ExternalSystem()

    def test_01_cannot_create_cart_when_client_id_is_missing(self):
        body = {'client_id': None, 'password': 'password'}
        request = Request(Request.HTTP_POST_METHOD, '/createCart', body)

        response = self.system.create_cart(request)

        self.assertTrue(response.is_bad_request())
        self.assertTrue(response.failed_with_message("Client ID is missing"))

    def test_02_cannot_create_cart_when_password_is_missing(self):
        body = {'client_id': 'client_id', 'password': None}
        request = Request(Request.HTTP_POST_METHOD, '/createCart', body)

        response = self.system.create_cart(request)

        self.assertTrue(response.is_bad_request())
        self.assertTrue(response.failed_with_message("Password is missing"))

    def test_03_can_create_cart_when_client_id_and_password_are_provided(self):
        body = {'client_id': 'client_id', 'password': 'password'}
        request = Request(Request.HTTP_POST_METHOD, '/createCart', body)

        response = self.system.create_cart(request)

        self.assertIsNotNone(response.content())
        self.assertTrue(response.is_successful())

    def test_04_cannot_add_to_cart_if_cart_id_is_missing(self):
        body = {'cart_id': None, 'book_isbn': 'Modern Software Engineering', 'book_quantity': 2}
        request = Request(Request.HTTP_POST_METHOD, '/addToCart', body)

        response = self.system.add_to_cart(request)

        self.assertTrue(response.is_bad_request())
        self.assertTrue(response.failed_with_message("Cart ID is missing"))

    def test_05_cannot_add_to_cart_if_book_isbn_is_missing(self):
        body = {'cart_id': 'cart_id', 'book_isbn': None, 'book_quantity': 2}
        request = Request(Request.HTTP_POST_METHOD, '/addToCart', body)

        response = self.system.add_to_cart(request)

        self.assertTrue(response.is_bad_request())
        self.assertTrue(response.failed_with_message("Book ISBN is missing"))

    def test_06_cannot_add_to_cart_if_book_quantity_is_missing(self):
        body = {'cart_id': 'cart_id', 'book_isbn': 'book_isbn', 'book_quantity': None}
        request = Request(Request.HTTP_POST_METHOD, '/addToCart', body)

        response = self.system.add_to_cart(request)

        self.assertTrue(response.is_bad_request())
        self.assertTrue(response.failed_with_message("Book Quantity is missing"))

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
        self.assertTrue(response.failed_with_message("Cart ID is missing"))

    def test_09_can_list_books_when_cart_exists(self):
        body = {'client_id': 'client_id', 'password': 'password'}
        request = Request(Request.HTTP_GET_METHOD, '/createCart', body)
        self.system.create_cart(request)
        body = {'cart_id': 'cart_id', 'book_isbn': 'Modern Software Engineering', 'book_quantity': 2}
        request = Request(Request.HTTP_GET_METHOD, '/addToCart', body)
        self.system.add_to_cart(request)

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
        self.assertTrue(response.failed_with_message("Cart ID is missing"))

    def test_11_cannot_checkout_cart_if_credit_card_number_is_missing(self):
        body = {'cart_id': 'cart_id',
                'credit_card_number': None,
                'credit_card_expiration_date': '399',
                'credit_card_owner': 'John Doe'}
        request = Request(Request.HTTP_POST_METHOD, '/checkoutCart', body)

        response = self.system.checkout_cart(request)

        self.assertTrue(response.is_bad_request())
        self.assertTrue(response.failed_with_message("Credit Card Number is missing"))

    def test_12_cannot_checkout_cart_if_credit_card_expiration_date_is_missing(self):
        body = {'cart_id': 'cart_id',
                'credit_card_number': '1234567890',
                'credit_card_expiration_date': None,
                'credit_card_owner': 'John Doe'}
        request = Request(Request.HTTP_POST_METHOD, '/checkoutCart', body)

        response = self.system.checkout_cart(request)

        self.assertTrue(response.is_bad_request())
        self.assertTrue(response.failed_with_message("Credit Card Expiration Date is missing"))

    def test_13_cannot_checkout_cart_if_credit_card_owner_is_missing(self):
        body = {'cart_id': 'cart_id',
                'credit_card_number': '1234567890',
                'credit_card_expiration_date': '399',
                'credit_card_owner': None}
        request = Request(Request.HTTP_POST_METHOD, '/checkoutCart', body)

        response = self.system.checkout_cart(request)

        self.assertTrue(response.is_bad_request())
        self.assertTrue(response.failed_with_message("Credit Card Owner is missing"))

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
        self.assertTrue(response.failed_with_message("Client ID is missing"))

    def test_16_cannot_list_purchases_if_password_is_missing(self):
        body = {'client_id': 'client_id', 'password': None}
        request = Request(Request.HTTP_GET_METHOD, 'listPurchases', body)

        response = self.system.list_purchases(request)

        self.assertTrue(response.is_bad_request())
        self.assertTrue(response.failed_with_message("Password is missing"))

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
