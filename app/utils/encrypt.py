# -*- coding: utf-8 -*-
import base64
from hashlib import sha256

def encrypt_password(password):
    """Hash password on the fly."""
    assert isinstance(password, str)
    
    if isinstance(password, str):
        password = password.encode('UTF-8')

    assert isinstance(password, bytes)

    result = password
    for i in range(10):
        result = sha256(result).digest()

    result = base64.b64encode(result)
    return result.decode('UTF-8')

def validate_password(password, hashed):
    return encrypt_password(password) == hashed
