"""
Application Bootstrap.
"""

from core.application.context import ApplicationContext

from core.application.environment import Environment
from core.application.runtime import ApplicationRuntime

from core.framework.bootstrap.service_registry import ServiceRegistry
from core.framework.container import ServiceContainer
from core.framework.logging import LoggerManager
from core.framework.settings import SettingsManager


class Bootstrap:
    """
    ERP Bootstrap.
    """

    @staticmethod
    def initialize() -> ApplicationContext:

        container = ServiceContainer()

        ServiceRegistry(container).register()

        return ApplicationContext(
            environment=container.resolve(Environment),
            runtime=container.resolve(ApplicationRuntime),
            settings=container.resolve(SettingsManager),
            logger=container.resolve(LoggerManager),
            container=container,
        )