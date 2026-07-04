from dataclasses import dataclass

from core.application.environment import Environment
from core.application.runtime import ApplicationRuntime

from core.framework.container import ServiceContainer
from core.framework.logging import LoggerManager
from core.framework.settings import SettingsManager


@dataclass(slots=True)
class ApplicationContext:
    """
    Root Application Context.

    Holds all framework services required by the ERP.
    """

    environment: Environment

    runtime: ApplicationRuntime

    settings: SettingsManager

    logger: LoggerManager

    container: ServiceContainer