from core.framework.container import ServiceContainer
from core.framework.logging import LoggerManager

container = ServiceContainer()

LoggerManager.initialize()

container.register_singleton(
    LoggerManager,
    LoggerManager,
)

logger = container.resolve(LoggerManager)

log = logger.get_logger()

log.info("Container Working")