"""
Sidebar Item Model.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class SidebarItem:
    """
    Represents one sidebar item.
    """

    title: str

    route: str

    icon: str = ""

    enabled: bool = True

    visible: bool = True