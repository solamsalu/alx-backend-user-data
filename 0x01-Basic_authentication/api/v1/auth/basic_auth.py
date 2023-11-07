#!/usr/bin/env python3
"""
Basic Auth module
"""

from api.v1.auth.auth import Auth
from typing import TypeVar, List
from models.user import User
import base64
import binascii


class BasicAuth(Auth):
    """
    class BasicAuth
    """

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """
         returns the Base64 part of the Authorization
         header for a Basic Authentication
        """
        if (authorization_header is None or
                not isinstance(authorization_header, str) or
                not authorization_header.startswith("Basic")):
            return None

        return authorization_header[6:]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """
        returns the decoded value of a Base64
        string base64_authorization_header
        """
        b64_auth_header = base64_authorization_header
        if b64_auth_header and isinstance(b64_auth_header, str):
            try:
                encode = b64_auth_header.encode('utf-8')
                base = base64.b64decode(encode)
                return base.decode('utf-8')
            except binascii.Error:
                return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """
        returns the user email and password from the Base64 decoded value.
        """
        decoded_64 = decoded_base64_authorization_header
        if (decoded_64 and isinstance(decoded_64, str) and
                ":" in decoded_64):
            res = decoded_64.split(":", 1)
            return (res[0], res[1])
        return (None, None)

    def current_user(self, request=None) -> TypeVar('User'):
        """
        overloads Auth and retrieves the User instance for a request
        """
        header = self.authorization_header(request)
        b64header = self.extract_base64_authorization_header(header)
        decoded = self.decode_base64_authorization_header(b64header)
        user_creds = self.extract_user_credentials(decoded)
        return self.user_object_from_credentials(*user_creds)

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """Return the User instance based on email and password."""
        if not all(map(lambda x: isinstance(x, str), (user_email, user_pwd))):
            return None
        try:
            # Search for the user in the database
            user = User.search(attributes={'email': user_email})
        except Exception:
            return None
        # Return None if there is no user in the database with the given email
        if not user:
            return None
        # Get the first user from the search results
        user = user[0]
        # Return None if the password is invalid
        if not user.is_valid_password(user_pwd):
            return None
        # Return the user instance
        return user

    def current_user(self, request=None) -> TypeVar('User'):
        """Retrieves the User instance for a request.

        Args:
            request (:obj:`Request`, optional): The request object. Defaults
            to None.

        Returns:
            User: The User instance based on the request.
        """
        # Get the authorization header from the request
        auth_header = self.authorization_header(request)
        # Extract the Base64 encoded string from the authorization header
        b64_auth_header = self.extract_base64_authorization_header(auth_header)
        # Decode the Base64 encoded string
        dec_header = self.decode_base64_authorization_header(b64_auth_header)
        # Extract the user email and password from the decoded Base64 string
        user_email, user_pwd = self.extract_user_credentials(dec_header)
        # Return the User instance based on the user email and password
        return self.user_object_from_credentials(user_email, user_pwd)
