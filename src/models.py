import config


class PasswordValidator:
    rules = config.PASSWORD_RULES
    invalidate_msg = config.INVALIDATE_MSG

    class PasswordValidationError(Exception):
        pass

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner=None):
        return vars(instance).get(self.name)

    def __set__(self, instance, value):
        if self.rules.match(value):
            vars(instance)[self.name] = value
        else:
            raise self.PasswordValidationError(self.invalidate_msg)


class User:
    password = PasswordValidator()

    def __init__(self, name, password, db):
        self.name = name
        self.password = password
        self.db = db

    def add_to_db(self):
        self.db.add_new_user(self.name, self.password)

    def delete_from_db(self):
        self.db.delete_user(self.name)

    def __repr__(self):
        return f'User(name={self.name}, password={self.password})'


class UserPasswordManager:

    class AuthorizationError(Exception):
        pass

    def __init__(self, name, password, db):
        self.user_name = name
        self.db = db
        self._authorization(self.user_name, password)

    def _authorization(self, name, password):
        if not self.db.is_user_exist(name) and not self.db.is_valid_password(name, password):
            raise self.AuthorizationError('invalid username/password')
        print(f'User {name} is authorized successfully!')
        self.db.set_user_id(name)

    def all_resources_info(self):
        return self.db.get_all_resources_info()

    def add_resource(self, resource, resource_password, comments=''):
        self.db.add_resource(resource, resource_password, comments)

    def update_resource(self, resource, new_password):
        self.db.update_password(resource, new_password)

    def extract_resource(self, resource):
        return self.db.retrieve_resource(resource)

    def delete_resource(self, resource):
        self.db.delete_resource(resource)

