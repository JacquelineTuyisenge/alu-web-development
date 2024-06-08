#!/usr/bin/env python3
"""
Main file
"""
from auth import Auth

email = 'jacky@bob.com'
password = 'MyPassKey123'
auth = Auth()

user = auth.register_user(email, password)
print(user.email, '@@@@', user, user.id)

print(auth.create_session(email))
print(auth.create_session("unknown@email.com"))
