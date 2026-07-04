"""
Application Environment Manager.

Loads and provides access to environment configuration.
"""

from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv
import os


@dataclass(frozen=True)
class Environment:
    """Application environment configuration."""

    APP_NAME: str
    APP_ENV: str
    APP_DEBUG: bool
    APP_VERSION: str
    API_BASE_URL: str
    TIMEZONE: str
    LANGUAGE: str
    LOG_LEVEL: str

    @classmethod
    def load(cls) -> "Environment":
        """Load configuration from the .env file."""

        project_root = Path(__file__).resolve().parents[2]
        env_file = project_root / ".env"

        if env_file.exists():
            load_dotenv(env_file)

        return cls(
            APP_NAME=os.getenv("APP_NAME", "ORM Repair ERP"),
            APP_ENV=os.getenv("APP_ENV", "development"),
            APP_DEBUG=os.getenv("APP_DEBUG", "True").lower() == "true",
            APP_VERSION=os.getenv("APP_VERSION", "1.0.0"),
            API_BASE_URL=os.getenv("API_BASE_URL", ""),
            TIMEZONE=os.getenv("TIMEZONE", "Asia/Kolkata"),
            LANGUAGE=os.getenv("LANGUAGE", "en"),
            LOG_LEVEL=os.getenv("LOG_LEVEL", "INFO"),
        )