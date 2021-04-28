import pytest
from database.sqlite_db import SqliteDatabase
from src.models import User, PasswordValidator


@pytest.fixture(scope='module', name='db')
def connect_to_db():
    db = SqliteDatabase('test.db')
    return db


def test_password_validation(db: SqliteDatabase):
    with pytest.raises(PasswordValidator.PasswordValidationError):
        user = User('Vova', '^asdfg#', db)


def test_add_user(db: SqliteDatabase):
    user = User('Arina', 'asdfgASD123', db)
    user.add_to_db()
    assert db.is_user_exist('Arina') is True


def test_delete_user(db: SqliteDatabase):
    user = User('Arina', 'asdfgASD123', db)
    user.delete_from_db()
    assert db.is_user_exist('Arina') is False
