"""
Dialog Contract.
"""

from abc import ABC, abstractmethod


class DialogContract(ABC):

    @abstractmethod
    def open(self) -> None:
        ...

    @abstractmethod
    def close(self) -> None:
        ...