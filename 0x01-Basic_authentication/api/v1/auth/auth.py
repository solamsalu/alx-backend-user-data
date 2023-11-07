#!/usr/bin/env python3
"""
Module for authentication
"""
from flask import request
from typing import List, TypeVar


User = TypeVar('User')
class Auth:
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Determine if the path requires authentication."""
        if not excluded_paths or not path:
            return True
        path = path if path.endswith('/') else path + '/'
        for excluded_path in excluded_paths:
            if path.startswith(excluded_path.strip("*")):
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """Get the authorization header from the request."""
        if not request or 'Authorization' not in request.headers:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> User:
        """Get the current user from the request."""
        return None  # This method will be implemented later
