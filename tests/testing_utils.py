import unittest
from src.utils import *


class UtilsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.password = create_password()

    def test_create_password(self) -> None:
        self.assertEqual(len(self.password), 10)
        self.assertRegex(self.password, r'[0-9a-zA-z]{10}')

    def test_password_encryption(self) -> None:
        hashed_password = encrypt_password(self.password)
        self.assertIsInstance(hashed_password, bytes)
        self.assertTrue(is_valid_password(self.password))

    def test_valid_password(self) -> None:
        self.assertTrue(is_valid_password(self.password))

    def test_pretty_display(self) -> None:
        test_data = [{'name': 'John', 'age': 50},
                     {'name': 'Kate', 'age': 25}]
        pd = pretty_display_recs(test_data)
        self.assertIsInstance(pd, str)
        self.assertEqual(pd, 'name = John\nage = 50\n\nname = Kate\nage = 25')


if __name__ == '__main__':
    unittest.main()
