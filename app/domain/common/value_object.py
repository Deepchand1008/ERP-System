"""
Value Object.
"""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ValueObject:
    """
    Base Value Object.
    """