"""
Base contract for repositories.
"""

from abc import ABC, abstractmethod
from typing import Any


class RepositoryContract(ABC):

    @abstractmethod
    def get(self, identifier: Any) -> Any:
        """Return one record."""

    @abstractmethod
    def list(self) -> list[Any]:
        """Return all records."""

    @abstractmethod
    def create(self, data: Any) -> Any:
        """Create record."""

    @abstractmethod
    def update(self, identifier: Any, data: Any) -> Any:
        """Update record."""

    @abstractmethod
    def delete(self, identifier: Any) -> bool:
        """Delete record."""