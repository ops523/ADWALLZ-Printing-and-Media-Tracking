"""
Password hashing and verification
"""

import bcrypt


def hash_password(password: str) -> str:

    salt = bcrypt.gensalt()

    return bcrypt.hashpw(
        password.encode(),
        salt
    ).decode()


def verify_password(
    plain_password: str,
    hashed_password: str
) -> bool:

    return bcrypt.checkpw(
        plain_password.encode(),
        hashed_password.encode()
    )


def create_default_password():

    return hash_password("admin123")
