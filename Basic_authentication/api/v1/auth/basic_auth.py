#!/usr/bin/env python3
'''Basic Auth class that inherits from Auth'''

from flask import request
from typing import List, TypeVar
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    pass
