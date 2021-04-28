import unittest
from database.db_datetime import *


class TestDbDate(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.db_date_now = DbDate()
        cls.db_date_str = DbDate('31/10/20 17:30:15')

    def test_init_with_no_args(self):
        self.assertEqual(self.db_date_now.date.date(), datetime.now().date())

    def test_init_with_str_arg(self):
        self.assertIsInstance(self.db_date_str.date, str)
        self.assertEqual(self.db_date_str.date, '31/10/20 17:30:15')

    def test_init_with_datetime_arg(self):
        db_date = DbDate(datetime(2020, 10, 31, 10, 30, 0))
        self.assertIsInstance(db_date.date, datetime)
        self.assertEqual(db_date.date, datetime(2020, 10, 31, 10, 30, 0))

    def test_format_date_to_str(self):
        db_date_str = self.db_date_now.format_date_to_string()
        self.assertEqual(db_date_str, datetime.now().strftime(self.db_date_now.pattern))

    def test_format_date_to_str_exception(self):
        self.assertRaises(TypeError, self.db_date_str.format_date_to_string)

    def test_format_str_to_date(self):
        db_date = self.db_date_str.format_string_to_date()
        self.assertEqual(db_date, datetime.strptime(self.db_date_str.date, self.db_date_str.pattern))

    def test_format_str_to_date_exception(self):
        self.assertRaises(TypeError, self.db_date_now.format_string_to_date)


if __name__ == '__main__':
    unittest.main()
