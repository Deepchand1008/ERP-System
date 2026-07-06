"""
Application Bootstrap.

Responsible for initializing the ERP framework.
"""

from core.application.context import ApplicationContext
from core.application.environment import Environment
from core.application.runtime import ApplicationRuntime

from core.framework.container import ServiceContainer
from core.framework.logging import LoggerManager
from core.framework.settings import SettingsManager


class Bootstrap:

    @staticmethod
    def initialize() -> ApplicationContext:
        """
        Initialize application framework.
        """

        LoggerManager.initialize()

        runtime = ApplicationRuntime()

        environment = Environment.load()

        settings = SettingsManager()

        settings.load()

        container = ServiceContainer()

        context = ApplicationContext(
            environment=environment,
            runtime=runtime,
            settings=settings,
            logger=LoggerManager(),
            container=container,
        )

        return context