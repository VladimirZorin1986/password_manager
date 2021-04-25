import secrets
import string
import bcrypt


ALPHABET = string.ascii_letters + string.digits


def create_password(alphabet: str = ALPHABET, length: int = 10) -> str:
    """
    Creates password from giving alphabet with given length
    """
    return ''.join(secrets.choice(alphabet) for _ in range(length))


def encrypt_password(password: str) -> bytes:
    """
    Generates hash from given password
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def is_valid_password(password: str):
    """
    Checks whether given password equals password from database
    """
    return bcrypt.checkpw(password.encode(), encrypt_password(password))


def pretty_display(records: list) -> str:
    """
    Returns list of records in pretty format
    """
    format_recs = []
    for record in records:
        format_rec = '\n'.join(f'{attr} = {record[attr]}' for attr in record.keys())
        format_recs.append(format_rec)
    return '\n\n'.join(format_recs)







