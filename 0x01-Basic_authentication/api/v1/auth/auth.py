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
        # Returns True if path is None
        if path is None:
            return True

        # Returns True if excluded_paths is None or empty
        if not excluded_paths:
            return True

        # Normalize the path to ensure slash tolerance
        path = path.strip('/')

        for pattern in excluded_paths:
            # Assuming excluded_paths contains paths ending with a '/',
            # we normalize them by stripping the slash
            pattern = pattern.rstrip('/')
            if path == pattern or path.startswith(pattern + '/'):
                return False

        # If the path is not in excluded_paths, return True
        return True

    def authorization_header(self, request=None) -> str:
        """Get the authorization header from the request."""
        return None  # This method will be implemented later

    def current_user(self, request=None) -> User:
        """Get the current user from the request."""
        return None  # This method will be implemented later
