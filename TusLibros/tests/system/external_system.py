import unittest

from system.external_system import ExternalCartSystem


class ExternalTests(unittest.TestCase):

    def setUp(self):
        self.system = ExternalCartSystem()

    def test_01_cannot_create_cart_when_client_id_is_missing(self):
        client_id = None

        self._assert_parameter_is_required_for_cart_creation(client_id, self._a_password(), "Client ID")

    def test_02_cannot_create_cart_when_password_is_missing(self):
        password = None

        self._assert_parameter_is_required_for_cart_creation(self._a_client_id(), password, "Password")

    def _assert_parameter_is_required_for_cart_creation(self, client_id, password, parameter_name_to_validate):
        with self.assertRaises(ValueError) as context:
            self.system.create_cart(client_id, password)
        self.assertEqual(str(context.exception), f'{parameter_name_to_validate} is missing')

    def _a_client_id(self):
        return 'client_id'

    def _a_password(self):
        return 'password'


if __name__ == '__main__':
    unittest.main()