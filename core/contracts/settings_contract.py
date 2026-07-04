"""
Settings Contract.
"""

from abc import ABC, abstractmethod


class SettingsContract(ABC):

    @abstractmethod
    def load(self) -> None:
        ...

    @abstractmethod
    def save(self) -> None:
        ...