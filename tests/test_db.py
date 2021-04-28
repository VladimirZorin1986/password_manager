import pytest
from database.sqlite_db import SqliteDatabase


@pytest.fixture(scope='module', name='db')
def get_connection():
    db = SqliteDatabase('test.db')
    return db


@pytest.mark.run(order=1)
def test_add_user(db):
    db.add_new_user('Vova', 'qwerty')
    assert db.is_user_exist('Vova') is True
    db.add_new_user('Anya', 'abcde')
    assert db.is_user_exist('Anya') is True
    db.add_new_user('John', 'ghjtyu')
    assert db.is_user_exist('John') is True


@pytest.mark.run(order=2)
def test_exception_add_user(db):
    with pytest.raises(db.UserExistError):
        db.add_new_user('Vova', '123456')


@pytest.mark.run(order=3)
def test_delete_user(db):
    db.delete_user('John')
    assert db.is_user_exist('John') is False


@pytest.mark.run(order=4)
def test_exception_delete_user(db):
    with pytest.raises(db.UserDoesNotExistError):
        db.delete_user('John')


@pytest.mark.run(order=5)
def test_is_valid_password(db):
    assert db.is_valid_password('Vova', 'qwerty') is True
    assert db.is_valid_password('Anya', 'qwerty') is False


@pytest.mark.run(order=6)
def test_set_user_id(db):
    user_id = db.set_user_id('Vova')
    assert user_id == 1


@pytest.mark.run(order=7)
def test_add_resource(db):
    db.add_resource('google.com', '123456789', 'my comments')
    db.add_resource('yandex.ru', '987654321')
    assert db.set_user_id('Anya') == 2
    db.add_resource('google.com', 'qwerty')
    assert db.is_resource_exist('google.com')


@pytest.mark.run(order=8)
def test_exception_add_resource(db):
    with pytest.raises(db.ResourceExistError):
        db.add_resource('google.com', 'asdfg')


@pytest.mark.run(order=9)
def test_retrieve_password(db):
    res = db.retrieve_resource('google.com')
    assert res['resource'] == 'google.com'


@pytest.mark.run(order=10)
def test_exception_retrieve_password(db):
    with pytest.raises(db.ResourceDoesNotExistError):
        db.retrieve_resource('yandex.ru')


@pytest.mark.run(order=11)
def test_update_password(db):
    db.update_password('google.com', 'love', 'new_pass')
    assert db.retrieve_resource('google.com')['password'] == 'love'


@pytest.mark.run(order=12)
def test_delete_resource(db):
    db.delete_resource('google.com')
    assert db.is_resource_exist('google.com') is False


@pytest.mark.run(order=13)
def test_get_all_resources_info(db):
    assert db.set_user_id('Vova') == 1
    results = db.get_all_resources_info()
    assert {res['resource'] for res in results} == {'google.com', 'yandex.ru'}


@pytest.mark.run(order=14)
def test_disconnect(db):
    db.close_db()
    assert 1 == 1



