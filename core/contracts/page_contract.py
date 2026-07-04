"""
Page Contract.
"""

from abc import ABC, abstractmethod


class PageContract(ABC):

    @abstractmethod
    def load(self) -> None:
        ...

    @abstractmethod
    def refresh(self) -> None:
        ...