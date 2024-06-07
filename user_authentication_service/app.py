#!/usr/bin/env python3
'''basic flask app'''

from flask import Flask, jsonify
from auth import  Auth

AUTH = Auth()
app = Flask(__name__)

app.url_map.strict_slashes = False


@app.route('/')
def hello_there():
    """hello there"""
    return jsonify({"message": "Bienvenue"})
