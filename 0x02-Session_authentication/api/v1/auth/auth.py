#!/usr/bin/env python3
""" Module fot authentication
"""

from flask import request
from typing import List, TypeVar
import fnmatch
import os


class Auth:
    """ Authentication class
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """checks if authentication is required for a given path"""
        if path is None:
            return True
        if excluded_paths is None or not excluded_paths:
            return True
        for excluded_path in excluded_paths:
            if fnmatch.fnmatch(path, excluded_path):
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """retrieves the authorization header from the request"""
        if request is None:
            return None
        return request.headers.get('Authorization', None)

    def current_user(self, request=None) -> TypeVar('User'):
        """retrieves the current user based on the request"""
        return None
    
    def session_cookie(self, request=None):
        """ Returns a cookie value from a request
        """
        if request is None:
            return None
        cookie_name = os.getenv("SESSION_NAME", "_my_sessio_id")
        return request.cookies.get(cookie_name)
