"""
Enterprise Dependency Injection Container.

Provides singleton service registration and resolution.
"""

from typing import Any


class ServiceContainer:
    """
    Dependency Injection Container.
    """

    def __init__(self) -> None:
        self._services: dict[type, Any] = {}

    def register_singleton(
        self,
        interface: type,
        instance: Any,
    ) -> None:
        """
        Register singleton instance.
        """

        self._services[interface] = instance

    def resolve(
        self,
        interface: type,
    ) -> Any:
        """
        Resolve registered service.
        """

        if interface not in self._services:
            raise ValueError(
                f"{interface.__name__} is not registered."
            )

        return self._services[interface]

    def contains(
        self,
        interface: type,
    ) -> bool:
        """
        Check registration.
        """

        return interface in self._services

    def clear(self) -> None:
        """
        Remove all services.
        """

        self._services.clear()