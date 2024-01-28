import unittest

from system.internal_system import InternalCartSystem


class InternalTests(unittest.TestCase):
    def test_cannot_create_cart_when_client_id_is_missing(self):
        system = InternalCartSystem()
        client_id = None
        password = 'password'

        response = system.create_cart(client_id, password)

        #self.assertRaises(ValueError, response)
        self.assertEqual('Client ID is missing', response)

    def test_cannot_create_cart_when_password_is_missing(self):
        system = InternalCartSystem()
        client_id = 'client_id'
        password = None

        response = system.create_cart(client_id, password)

        #self.assertRaises(ValueError, response)
        self.assertEqual('Password is missing', response)

    def test_can_create_cart_when_client_id_and_password_are_provided(self):
        system = InternalCartSystem()
        client_id = 'client_id'
        password = 'password'

        response = system.create_cart(client_id, password)

        self.assertIsNotNone(response)




if __name__ == '__main__':
    unittest.main()
