import unittest

from business.catalogue import Catalogue
from system.internal_system import InternalSystem


class InternalSystemTests(unittest.TestCase):

    def setUp(self):
        self._system = InternalSystem()
        self._catalogue = Catalogue()

    def test_01_can_create_cart_when_credentials_are_provided(self):
        cart_id = self._system.create_cart(self._a_client_id(), self._a_password())

        self._assert_is_valid(cart_id)

    def test_02_can_add_books_when_cart_is_created(self):
        cart_id = self._system.create_cart(self._a_client_id(), self._a_password())
        expected_books = [self._catalogue.a_book()]

        result_of_cart_addition = self._system.add_to_cart(
            cart_id,
            self._catalogue.a_book(),
            self._catalogue.DEFAULT_QUANTITY
        )

        self._assert_books_were_successfully_added_to_cart_for(cart_id, expected_books)
        self.assertTrue(result_of_cart_addition, self._system.SUCCESS_RESPONSE)

    def test_03_can_list_books_when_cart_is_created(self):
        cart_id = self._system.create_cart(self._a_client_id(), self._a_password())
        self._system.add_to_cart(cart_id, self._catalogue.a_book(), self._catalogue.DEFAULT_QUANTITY)

        current_books_in_cart = self._system.list_cart(cart_id)

        self._assert_book_isbn_and_quantity_is_valid_for(current_books_in_cart, cart_id)

    def test_04_cannot_add_books_when_cart_does_not_exist(self):
        non_existing_cart_id = self._an_invalid_cart_id()

        self._assert_cannot_add_books_to_non_existing_cart(non_existing_cart_id)

    def test_05_cannot_list_books_when_cart_does_not_exist(self):
        non_existing_cart_id = self._an_invalid_cart_id()

        self._assert_cannot_list_books_to_non_existing_cart(non_existing_cart_id)

    def test_06_can_have_multiple_carts(self):
        cart_id = self._system.create_cart(self._a_client_id(), self._a_password())
        another_cart_id = self._system.create_cart(self._a_client_id(), self._a_password())

        self.assertNotEquals(cart_id, another_cart_id)

    def test_07_can_add_books_to_multiple_carts(self):
        cart_id = self._system.create_cart(self._a_client_id(), self._a_password())
        another_cart_id = self._system.create_cart(self._a_client_id(), self._a_password())

        self._system.add_to_cart(cart_id, self._catalogue.a_book(), self._catalogue.DEFAULT_QUANTITY)
        self._system.add_to_cart(another_cart_id, self._catalogue.another_book(), self._catalogue.DEFAULT_QUANTITY)

        self._assert_books_were_successfully_added_to_cart_for(cart_id, [self._catalogue.a_book()])
        self._assert_books_were_successfully_added_to_cart_for(another_cart_id, [self._catalogue.another_book()])

    def _assert_book_isbn_and_quantity_is_valid_for(self, current_books_in_cart, cart_id):
        self.assertEqual([f"{self._catalogue.a_book()}|{cart_id}"], current_books_in_cart)

    def _assert_cannot_perform_action_when_cart_does_not_exist(self, non_existing_cart_id, system_action_on):
        with self.assertRaises(ValueError) as context:
            system_action_on(non_existing_cart_id)
        self.assertEqual(str(context.exception), 'Cart does not exist')

    def _assert_cannot_add_books_to_non_existing_cart(self, non_existing_cart_id):
        self._assert_cannot_perform_action_when_cart_does_not_exist(
            non_existing_cart_id,
            lambda cart_id: self._system.add_to_cart(cart_id, self._catalogue.a_book(), self._catalogue.DEFAULT_QUANTITY)
        )

    def _assert_cannot_list_books_to_non_existing_cart(self, non_existing_cart_id):
        self._assert_cannot_perform_action_when_cart_does_not_exist(
            non_existing_cart_id,
            lambda cart_id: self._system.list_cart(cart_id)
        )

    def _assert_books_were_successfully_added_to_cart_for(self, cart_id, expected_books):
        current_books_in_cart = self._system.list_cart(cart_id)
        self.assertTrue(expected_books, current_books_in_cart)

    def _a_client_id(self):
        return 'client_id'

    def _a_password(self):
        return 'password'

    def _an_invalid_cart_id(self):
        return 'cart_id'

    def _assert_is_valid(self, cart_id):
        try:
            int(cart_id)
        except ValueError:
            self.fail("Cart ID is not valid")


if __name__ == '__main__':
    unittest.main()
