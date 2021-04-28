from abc import ABCMeta, abstractmethod
from .db_datetime import DbDate


class Database(metaclass=ABCMeta):
    class UserExistError(Exception):
        pass

    class UserDoesNotExistError(Exception):
        pass

    class ResourceExistError(Exception):
        pass

    class ResourceDoesNotExistError(Exception):
        pass

    class NoConnectionExist(Exception):
        pass

    def __init__(self, db_name) -> None:
        self.db_name = db_name
        self.db_date_cls = DbDate
        self.con = None
        self.user_id = None

    @abstractmethod
    def connect_to_db(self):
        ...

    @abstractmethod
    def add_new_user(self, name: str, password: str) -> None:
        if self.is_user_exist(name):
            raise self.UserExistError("user already exist")
        ...

    @abstractmethod
    def is_user_exist(self, name: str) -> bool:
        ...

    @abstractmethod
    def delete_user(self, name: str) -> None:
        if not self.is_user_exist(name):
            raise self.UserDoesNotExistError('user does not exist')
        ...

    @abstractmethod
    def is_valid_password(self, name, password):
        ...

    @abstractmethod
    def set_user_id(self, name):
        ...

    @abstractmethod
    def is_resource_exist(self, resource: str) -> bool:
        ...

    @abstractmethod
    def add_resource(self, resource, resource_password, comments=''):
        if self.is_resource_exist(resource):
            raise self.ResourceExistError('resource exist for this user')
        ...

    @abstractmethod
    def update_password(self, resource, new_password, comments=''):
        if not self.is_resource_exist(resource):
            raise self.ResourceDoesNotExistError('resource does not exist')
        ...

    @abstractmethod
    def retrieve_resource(self, resource):
        if not self.is_resource_exist(resource):
            raise self.ResourceDoesNotExistError('resource does not exist')
        ...

    @abstractmethod
    def delete_resource(self, resource):
        if not self.is_resource_exist(resource):
            raise self.ResourceDoesNotExistError('resource does not exist')
        ...

    @abstractmethod
    def get_all_resources_info(self):
        ...

    @abstractmethod
    def close_db(self):
        if self.con is None:
            raise self.NoConnectionExist('no connection to database exist')
        ...

    def __enter__(self):
        self.connect_to_db()
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.close_db()
        return False
