"""
Window Contract.
"""

from abc import ABC, abstractmethod


class WindowContract(ABC):

    @abstractmethod
    def initialize(self) -> None:
        ...

    @abstractmethod
    def build(self) -> None:
        ...

    @abstractmethod
    def connect_signals(self) -> None:
        ...