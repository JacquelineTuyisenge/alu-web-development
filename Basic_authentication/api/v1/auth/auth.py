#!/usr/bin/env python3
'''Auth class to manage API authentication'''

from flask import request
from typing import List, TypeVar


class Auth:
    '''Auth class to manage the API authentication'''

    def require_auth(self, path: str, excluded_paths: List[list]) -> bool:
        '''Require authentication'''

        if path is None:
            return True
        if not excluded_paths:
            return True
        # if not path.endswith('/'):
        #     path += '/'
        if not path.endswith('*'):
            path += '*'
        if path in excluded_paths:
            return False
        for p in excluded_paths:
            if not p.endswith("*" ):
                p += "*"
            # if not p.endswith("/" ):
            #     p += "/"

            if path in p:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        '''Authorization header'''

        if request is None:
            return None
        if "Authorization" not in request.headers:
            return None
        return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar('User'):
        '''Current user'''
        return None
