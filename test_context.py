from core.application import (
    ApplicationContext,
    ApplicationRuntime,
    Environment,
)
from core.framework.container import ServiceContainer
from core.framework.logging import LoggerManager
from core.framework.settings import SettingsManager

LoggerManager.initialize()

context = ApplicationContext(
    environment=Environment.load(),
    runtime=ApplicationRuntime(),
    settings=SettingsManager(),
    logger=LoggerManager(),
    container=ServiceContainer(),
)

print(context.environment.APP_NAME)
print(context.runtime.environment)
print(context.settings.settings.theme)