from datetime import datetime
from typing import Union


class DbDate:
    PATTERN = '%d/%m/%y %H:%M:%S'

    def __init__(self, date: Union[datetime, str] = None):
        self.date = date or datetime.now()

    def format_date_to_string(self):
        if isinstance(self.date, datetime):
            return self.date.strftime(self.PATTERN)
        raise TypeError(f'must be datetime object, not {self.date.__class__.__name__}')

    def format_string_to_date(self):
        if isinstance(self.date, str):
            return datetime.strptime(self.date, self.PATTERN)
        raise TypeError(f'must be string, not {self.date.__class__.__name__}')