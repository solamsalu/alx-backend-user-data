#!/usr/bin/env python3
"""
Module for authentication
"""
from tabnanny import check
from flask import request
from typing import TypeVar, List
User = TypeVar('User')


class Auth:
    """
    a class to manage the API authentication
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        returns False - path and excluded_paths
        """
        # If path is None, return True
        if not path:
            return True
        # If excluded_paths is None or empty, return True
        if not excluded_paths:
            return True
        # Remove the trailing slash from the path
        path = path.rstrip("/")
        # Check if path is in excluded_paths and return False if path is
        # in excluded_paths
        # Loop through excluded paths
        for excluded_path in excluded_paths:
            # Check if given path starts with excluded path, with * at the end
            if excluded_path.endswith("*") and \
                    path.startswith(excluded_path[:-1]):
                # Return False if path starts with excluded path with * at end
                return False
            # Check if the given path is equal to the excluded path
            elif path == excluded_path.rstrip("/"):
                # Return False if the path is equal to the excluded path
                return False
        # If path is not in excluded_paths, return True
        return True

    def authorization_header(self, request=None) -> str:
        """
        returns None - request
        """
        if request is None:
            return None
        return request.headers.get("Authorization")

    def current_user(self, request=None) -> User:
        """
        returns None - request
        """
        return None
