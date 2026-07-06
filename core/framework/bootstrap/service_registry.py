"""
Framework Service Registry.

Registers all framework services into the dependency container.
"""

from core.application.environment import Environment
from core.application.runtime import ApplicationRuntime

from core.framework.container import ServiceContainer
from core.framework.logging import LoggerManager
from core.framework.settings import SettingsManager


class ServiceRegistry:
    """
    Registers framework services.
    """

    def __init__(self, container: ServiceContainer) -> None:
        self._container = container

    def register(self) -> None:
        """
        Register framework services.
        """

        LoggerManager.initialize()

        self._container.register_singleton(
            Environment,
            Environment.load(),
        )

        self._container.register_singleton(
            ApplicationRuntime,
            ApplicationRuntime(),
        )

        settings = SettingsManager()
        settings.load()

        self._container.register_singleton(
            SettingsManager,
            settings,
        )

        self._container.register_singleton(
            LoggerManager,
            LoggerManager(),
        )