import unittest

from system.internal_system import InternalCartSystem


class InternalTests(unittest.TestCase):

    def setUp(self):
        self.system = InternalCartSystem()
        self.client_id = self._a_client_id()
        self.password = self._a_password()
        self.book_isbn = self._a_book_isbn()

    def test_01_cannot_create_cart_when_client_id_is_missing(self):
        client_id = None

        self._assert_client_id_is_required_for_cart_creation(client_id)

    def test_02_cannot_create_cart_when_password_is_missing(self):
        password = None

        self._assert_password_is_required_for_cart_creation(password)

    def test_03_can_create_cart_when_client_id_and_password_are_provided(self):

        response = self.system.create_cart(self.client_id, self.password)

        self.assertIsNotNone(response)

    def test_04_cannot_add_to_cart_if_cart_id_is_missing(self):
        cart_id = None

        self._assert_cart_id_is_required_for_cart_addition(cart_id)

    def test_05_cannot_add_to_cart_if_client_id_is_missing(self):
        book_isbn = None

        self._assert_book_isbn_is_required_for_cart_addition(book_isbn)

    def test_06_cannot_add_to_cart_if_book_quantity_is_missing(self):
        book_quantity = None

        self._assert_book_quantity_is_required_for_cart_addition(book_quantity)

    def test_07_can_add_to_cart_if_cart_id_and_book_isbn_and_book_quantity_are_provided(self):
        # test_07_can_add_to_cart_if_required_parameters_are_provided?

        cart_id = self._a_cart_id()

        self.system.add_to_cart(cart_id, self.book_isbn, self._a_quantity_of_books())

        self._assert_cart_contains_added_book(cart_id)

    def _assert_client_id_is_required_for_cart_creation(self, client_id):
        try:
            _ = self.system.create_cart(client_id, self.password)
        except ValueError as exception:
            self.assertEqual(str(exception), 'Client ID is missing')

    def _assert_password_is_required_for_cart_creation(self, password):
        try:
            _ = self.system.create_cart(self.client_id, password)
        except ValueError as exception:
            self.assertEqual(str(exception), 'Password is missing')

    def _assert_cart_id_is_required_for_cart_addition(self, cart_id):
        try:
            _ = self.system.add_to_cart(cart_id, self.book_isbn, self._a_quantity_of_books())
        except ValueError as exception:
            self.assertEqual(str(exception), 'Cart ID is missing')

    def _assert_book_isbn_is_required_for_cart_addition(self, book_isbn):
        try:
            _ = self.system.add_to_cart(self._a_cart_id(), book_isbn, self._a_quantity_of_books())
        except ValueError as exception:
            self.assertEqual(str(exception), 'Book ISBN is missing')

    def _assert_book_quantity_is_required_for_cart_addition(self, book_quantity):
        try:
            _ = self.system.add_to_cart(self._a_cart_id(), self.book_isbn, book_quantity)
        except ValueError as exception:
            self.assertEqual(str(exception), 'Book Quantity is missing')

    def _assert_cart_contains_added_book(self, cart_id):
        self.assertTrue(self._a_cart_with(cart_id).contains_book(self.book_isbn))

    def _a_cart_with(self, cart_id):
        return self.system.cart_system[cart_id]['cart']

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
