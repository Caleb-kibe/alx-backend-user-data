#!/usr/bin/env python3
""" SessionAuth model for API
"""

from .auth import Auth
from uuid import uuid4
from models.user import User


class SessionAuth(Auth):
    """ SessionAuth class that inherits from Auth
    """
    
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ Creates a session ID for the user"""
        if user_id is None or not isinstance(user_id, str):
            return None

        session_id = str(uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return str(session_id)
    

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ Returns a user ID based on a session ID
        Args:
            session_id (str): session ID
        Return:
            user id or None if session_id is None or not a string
        """
        if session_id is None or not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)
    

    def current_user(self, request=None):
        """ returns a User instance based on a cookie value
        """
        if request is None:
            return None
        session_id = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_id)
        user = User.get(user_id)
        return user