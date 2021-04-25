import unittest
from utils import *


class PasswordTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.password = create_password()

    def test_create_password(self) -> None:
        self.assertEqual(len(self.password), 10)
        self.assertRegex(self.password, r'[0-9a-zA-z]{10}')

    def test_password_encryption(self) -> None:
        hashed_password = encrypt_password(self.password)
        self.assertIsInstance(hashed_password, bytes)
        self.assertTrue(check_password(self.password))




if __name__ == '__main__':
    unittest.main()
