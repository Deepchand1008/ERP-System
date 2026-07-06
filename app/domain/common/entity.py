"""
Base Entity.

All domain entities inherit from this class.
"""

from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID
from uuid import uuid4


@dataclass(slots=True)
class Entity:
    """
    Base entity.
    """

    id: UUID

    @classmethod
    def create(cls):
        return cls(id=uuid4())