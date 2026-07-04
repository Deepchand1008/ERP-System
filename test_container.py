from core.container import ServiceContainer
from core.logging import LoggerManager

container = ServiceContainer()

LoggerManager.initialize()

container.register_singleton(
    LoggerManager,
    LoggerManager,
)

logger = container.resolve(LoggerManager)

log = logger.get_logger()

log.info("Container Working")