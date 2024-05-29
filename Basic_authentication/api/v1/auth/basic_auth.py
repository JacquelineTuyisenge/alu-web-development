#!/usr/bin/env python3
'''Basic Auth class that inherits from Auth'''

from flask import request
from typing import List, TypeVar
from api.v1.auth.auth import Auth
from models.user import User
import base64


class BasicAuth(Auth):
    '''Basic Auth class that inherits from Auth'''

    def extract_base64_authorization_header(self, au_h: str) -> str:
        '''Extract base64 authorization header'''

        if not au_h:
            return None

        if type(au_h) != str:
            return None

        if not au_h.startswith("Basic "):
            return None
        return au_h.split(" ")[1:]
