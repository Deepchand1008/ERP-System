"""
Global Exception Handler.
"""

from loguru import logger

from .base_exception import ERPException


class ExceptionHandler:
    """
    Handles all ERP exceptions.
    """

    @staticmethod
    def handle(exception: Exception) -> None:
        """
        Handle application exception.
        """

        if isinstance(exception, ERPException):
            logger.error(exception.message)
        else:
            logger.exception(exception)