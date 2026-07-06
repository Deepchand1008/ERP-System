"""
Sidebar Section.
"""

from dataclasses import dataclass, field

from .sidebar_item import SidebarItem


@dataclass(slots=True)
class SidebarSection:
    """
    Sidebar section.
    """

    title: str

    items: list[SidebarItem] = field(default_factory=list)

    def add_item(self, item: SidebarItem) -> None:
        self.items.append(item)