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
            base64.b64decode(base64_authorization_header)
        except Exception:
            return None

        return base64_authorization_header.decode('utf-8')

    # def extract_user_credentials(
    #     self,
    #     decoded_base64_authorization_header: str
    # ) -> (str, str):
    #     '''Extract user credentials'''

    #     if not decoded_base64_authorization_header:
    #         return None, None