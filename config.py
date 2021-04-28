import re


PASSWORD_RULES = re.compile(r'^[0-9a-zA-z]{8,12}$')
INVALIDATE_MSG = 'password must contain 8 to 12 chars and consists of a-z, A-Z, 0-9 only'
DATE_PATTERN = '%d/%m/%y %H:%M:%S'
DB_NAME = 'sqlite_db'


