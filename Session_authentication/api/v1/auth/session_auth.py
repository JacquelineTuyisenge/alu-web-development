#!/usr/bin/env python3
'''Basic Auth class that inherits from Auth'''

from flask import request
# from typing import List, TypeVar
from api.v1.auth.auth import Auth
from models.user import User
# import base64


class SessionAuth(Auth):
    '''Session Auth class that inherits from Auth'''
