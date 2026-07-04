"""
Central Logging Manager.

Every module in the ERP must use this logger.
"""

from pathlib import Path

from loguru import logger

from core.application.paths import ApplicationPaths


class LoggerManager:
    """
    ERP Logger Manager.
    """

    @staticmethod
    def initialize() -> None:
        """Initialize application logging."""

        log_directory = ApplicationPaths.LOGS
        log_directory.mkdir(parents=True, exist_ok=True)

        logger.remove()

        logger.add(
            log_directory / "application.log",
            level="DEBUG",
            rotation="10 MB",
            retention="30 days",
            compression="zip",
            enqueue=True,
            backtrace=True,
            diagnose=True,
            format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}",
        )

        logger.add(
            log_directory / "error.log",
            level="ERROR",
            rotation="10 MB",
            retention="60 days",
            compression="zip",
            enqueue=True,
            backtrace=True,
            diagnose=True,
        )

    @staticmethod
    def get_logger():
        """Return Loguru logger instance."""
        return logger