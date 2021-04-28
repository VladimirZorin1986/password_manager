import unittest
from database.sqlite_db import SqliteDatabase


class TestDatabase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.db = SqliteDatabase()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.db.close_db()

    def test_save_user(self):
        self.db.save_user('Vova', 'qwerty')
        res = self.db.con.execute(
            'SELECT * FROM user WHERE name = ?',
            ('Vova', )
        ).fetchone()['name']
        self.assertEqual(res, 'Vova')

    def test_is_user_exist(self):
        self.assertTrue(self.db.is_user_exist('Vova'))

    def test_delete_user(self):
        self.db.delete_user('Vova')
        self.assertFalse(self.db.is_user_exist('Vova'))

    def test_is_valid_password(self):
        self.assertTrue(self.db.is_valid_password('Vova', 'qwerty'))

    def test_set_user_id(self):
        user_id = self.db.set_user_id('Vova')
        print(self.db.user_id)
        self.assertEqual(user_id, self.db.user_id)

    def test_save_resource(self):
        self.db.save_resource('google.com', 'google_pw123', 'my comments')
        res = self.db.con.execute(
            'SELECT * FROM manager WHERE resource = ?',
            ('google.com', )
        ).fetchone()['name']
        self.assertEqual(res, 'google.com')







if __name__ == '__main__':
    unittest.main()
