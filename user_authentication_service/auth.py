#!/usr/bin/env python3
'''hash password'''

from user import Base, User
import bcrypt
from db import DB
from uuid import uuid4
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> str:
    '''hashing a password'''
    return bcrypt.hashpw(
        password.encode('utf-8'),
        bcrypt.gensalt()
        ).decode('utf-8')

    def _generate_uuid() -> str:
        '''generate a uuid'''
        return str(uuid4())

    class Auth:
        """Auth class to interact with the authentication database.
        """

        def __init__(self):
            self._db = DB()

        def register_user(self, email: str, password: str) -> User:
            '''registering a user'''
            try:
                already_exist_user = self._db.find_user_by(email=email)
                raise ValueError(f'User {email} already exists.')
            except NoResultFound:
                hashed_password = _hash_password(password)
                return self._db.add_user(email, hashed_password)
