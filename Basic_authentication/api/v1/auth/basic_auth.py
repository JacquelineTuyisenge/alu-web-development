#!/usr/bin/env python3
'''Basic Auth class that inherits from Auth'''

from flask import request
from typing import List, TypeVar
from api.v1.auth.auth import Auth
from models.user import User
import base64


class BasicAuth(Auth):
    '''Basic Auth class that inherits from Auth'''

    def extract_base64_authorization_header(
        self,
        authorization_header: str
    ) -> str:
        '''Extract base64 authorization header'''

        if not authorization_header:
            return None

        if type(authorization_header) != str:
            return None

        if not authorization_header.startswith("Basic "):
            return None

        return authorization_header.split(" ")[1]

    def decode_base64_authorization_header(
        self,
        base64_authorization_header: str
    ) -> str:
        '''Decode base64 authorization header'''

        if not base64_authorization_header:
            return None

        if type(base64_authorization_header) != str:
            return None

        try:
            return base64.b64decode(
                base64_authorization_header).decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(
        self,
        decoded_base64_authorization_header: str
    ) -> (str, str):
        '''Extract user credentials'''

        if not decoded_base64_authorization_header:
            return None, None

        if type(decoded_base64_authorization_header) != str:
            return None, None

        if ":" not in decoded_base64_authorization_header:
            return None, None

        username, password = decoded_base64_authorization_header.split(":", 1)

        return username, password

    def user_object_from_credentials(
        self,
        user_email: str,
        user_pwd: str
    ) -> TypeVar('User'):
        '''User object from credentials'''

        if not user_email or type(user_email) != str:
            return None

        if not user_pwd or type(user_pwd) != str:
            return None

        try:
            users = User.search({"email": user_email})
        except Exception:
            return None

        for user in users:
            if user.is_valid_password(user_pwd):
                return user

        return None

    def current_user(self, request=None) -> TypeVar('User'):
        '''Current user'''

        auth = self.authorization_header(request)
        extract = self.extract_base64_authorization_header(auth)
        decode = self.decode_base64_authorization_header(extract)
        credentials = self.extract_user_credentials(decode)
        user = self.user_object_from_credentials(*credentials)

        return user
