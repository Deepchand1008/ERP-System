"""
Aggregate Root.
"""

from dataclasses import dataclass, field

from .entity import Entity
from .domain_event import DomainEvent


@dataclass(slots=True)
class AggregateRoot(Entity):
    """
    Base Aggregate Root.
    """

    events: list[DomainEvent] = field(default_factory=list)

    def add_event(
        self,
        event: DomainEvent,
    ) -> None:

        self.events.append(event)

    def clear_events(self) -> None:

        self.events.clear()