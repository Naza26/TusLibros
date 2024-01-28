import unittest

from system.internal_system import InternalCartSystem


class InternalTests(unittest.TestCase):

    def setUp(self):
        self.system = InternalCartSystem()
        self.client_id = self._a_client_id()
        self.password = self._a_password()

    def test_01_cannot_create_cart_when_client_id_is_missing(self):
        client_id = None

        try:
            _ = self.system.create_cart(client_id, self.password)
        except ValueError as exception:
            self.assertEqual(str(exception), 'Client ID is missing')

    def test_02_cannot_create_cart_when_password_is_missing(self):
        password = None

        try:
            _ = self.system.create_cart(self.client_id, password)
        except ValueError as exception:
            self.assertEqual(str(exception), 'Password is missing')

    def test_03_can_create_cart_when_client_id_and_password_are_provided(self):

        response = self.system.create_cart(self.client_id, self.password)

        self.assertIsNotNone(response)

    def _a_client_id(self):
        return 'client_id'

    def _a_password(self):
        password = 'password'
        return password




if __name__ == '__main__':
    unittest.main()
