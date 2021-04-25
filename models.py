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
    db = config.DB

    def __init__(self, name, password):
        self.name = name
        self.password = password

    def add_to_db(self):
        self.db.save_user(self.name, self.password)

    def delete_from_db(self):
        self.db.delete_user(self.name)

    def __repr__(self):
        return f'User(name={self.name}, password={self.password})'


class UserPasswordManager:
    db = config.DB

    class AuthorizationError(Exception):
        pass

    def __init__(self, name, password):
        self.user_name = name
        self._authorization(self.user_name, password)
        self._all_resources_info = None

    def _authorization(self, name, password):
        if not self.db.is_exist_user(name) and not is_valid_password(password):
            raise self.AuthorizationError('invalid username/password')

    @property
    def all_resources_info(self):
        if self._all_resources_info is None:
            self._all_resources_info = self.db.get_all_resources_info(self.user_name)
        return self._all_resources_info

    def add_resource(self, resource, resource_password, comments=''):
        self.db.save_resource(self.user_name, resource, resource_password, comments)

    def update_resource(self, resource, new_password):
        self.db.update(self.user_name, resource, new_password)

    def extract_resource(self, resource):
        return self.db.retrieve(self.user_name, resource)

    def delete_resource(self, resource):
        self.db.delete_resource(self.user_name, resource)

