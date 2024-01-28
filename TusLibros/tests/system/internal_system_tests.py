import unittest

from system.internal_system import InternalCartSystem


class InternalTests(unittest.TestCase):

    def setUp(self):
        self.system = InternalCartSystem()
        self.client_id = self._a_client_id()
        self.password = self._a_password()

    def test_cannot_create_cart_when_client_id_is_missing(self):
        client_id = None

        response = self.system.create_cart(client_id, self.password)

        #self.assertRaises(ValueError, response)
        self.assertEqual('Client ID is missing', response)

    def test_cannot_create_cart_when_password_is_missing(self):
        password = None

        response = self.system.create_cart(self.client_id, password)

        #self.assertRaises(ValueError, response)
        self.assertEqual('Password is missing', response)

    def test_can_create_cart_when_client_id_and_password_are_provided(self):

        response = self.system.create_cart(self.client_id, self.password)

        self.assertIsNotNone(response)

    def _a_client_id(self):
        return 'client_id'

    def _a_password(self):
        password = 'password'
        return password




if __name__ == '__main__':
    unittest.main()
