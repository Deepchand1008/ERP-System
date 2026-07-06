"""
Domain Event.
"""

from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class DomainEvent:
    """
    Base Domain Event.
    """

    occurred_at: datetime