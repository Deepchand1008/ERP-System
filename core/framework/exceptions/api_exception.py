"""
API Exceptions.
"""

from .base_exception import ERPException


class ApiException(ERPException):
    """REST API related exception."""