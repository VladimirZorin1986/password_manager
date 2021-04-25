import re
from database import *

DB = Database()
PASSWORD_RULES = re.compile(r'^[0-9a-zA-z]{8,12}$')
INVALIDATE_MSG = 'password must contain 8 to 12 chars and consists of a-z, A-Z, 0-9 only'