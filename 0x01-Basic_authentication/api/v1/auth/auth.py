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
        if path is None or not excluded_paths:
            return True

        # Normalize the path to ensure slash tolerance
        path = path.strip('/')
        for pattern in excluded_paths:
            # Normalize the pattern to ensure slash tolerance
            pattern = pattern.strip('/')
            if path == pattern or path.startswith(pattern + '/'):
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """Get the authorization header from the request."""
        return None  # This method will be implemented later

    def current_user(self, request=None) -> User:
        """Get the current user from the request."""
        return None  # This method will be implemented later
