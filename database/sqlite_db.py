from .database_interface import Database
from src.utils import encrypt_password
import sqlite3
import bcrypt


class SqliteDatabase(Database):

    def connect_to_db(self):
        if self.con is None:
            self.con = sqlite3.connect(self.db_name)
            self.con.row_factory = sqlite3.Row

    def add_new_user(self, name: str, password: str) -> None:
        super().add_new_user(name, password)
        hashed_password = encrypt_password(password)
        with self.con:
            self.con.execute('INSERT INTO user (name, password, creation_dt) VALUES (?, ?, ?)',
                             (name, hashed_password, self.db_date_cls().format_date_to_string()))

    def is_user_exist(self, name: str) -> bool:
        result = self.con.execute('SELECT name FROM user WHERE name = ?', (name, )).fetchone()
        return result is not None

    def delete_user(self, name: str) -> None:
        super().delete_user(name)
        with self.con:
            self.con.execute('DELETE FROM user WHERE name = ?', (name, ))

    def is_valid_password(self, name, password):
        saved_password = self.con.execute(
            'SELECT password FROM user WHERE name = ?',
            (name, )
        ).fetchone()['password']
        return bcrypt.checkpw(password.encode(), saved_password)

    def set_user_id(self, name):
        self.user_id = self.con.execute(
            'SELECT id FROM user WHERE name = ?',
            (name, )
        ).fetchone()['id']
        return self.user_id

    def is_resource_exist(self, resource: str) -> bool:
        result = self.con.execute(
            'SELECT resource,user_id FROM manager WHERE resource = ? AND user_id = ?',
            (resource, self.user_id)).fetchone()
        return result is not None

    def add_resource(self, resource, resource_password, comments=''):
        super().add_resource(resource, resource_password, comments)
        with self.con:
            self.con.execute(
                '''INSERT INTO manager (resource, password, comments, user_id, last_updated)
                   VALUES (?, ?, ?, ?, ?)''',
                (resource, resource_password, comments,
                 self.user_id, self.db_date_cls().format_date_to_string())
            )

    def update_password(self, resource, new_password, comments=''):
        super().update_password(resource, new_password, comments)
        with self.con:
            self.con.execute(
                'UPDATE manager SET password = ?, comments = ? WHERE resource = ?',
                (new_password, comments, resource)
            )

    def retrieve_resource(self, resource):
        super().retrieve_resource(resource)
        result = self.con.execute(
            'SELECT resource, password, comments, last_updated FROM manager '
            'WHERE resource = ? AND user_id = ?',
            (resource, self.user_id)
        ).fetchone()
        return result

    def delete_resource(self, resource):
        super().delete_resource(resource)
        with self.con:
            self.con.execute(
                'DELETE FROM manager WHERE resource = ? AND user_id = ?',
                (resource, self.user_id)
            )

    def get_all_resources_info(self):
        results = self.con.execute(
            'SELECT resource, password, comments, last_updated FROM manager '
            'WHERE user_id = ?',
            (self.user_id, )
        ).fetchall()
        return results

    def close_db(self):
        super().close_db()
        self.con.close()
