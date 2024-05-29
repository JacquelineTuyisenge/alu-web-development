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
