"""
Base Exception for the ERP.
"""


class ERPException(Exception):
    """
    Base class for all ERP exceptions.
    """

    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message