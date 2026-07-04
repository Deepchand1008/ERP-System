
"""
Application metadata for the ORM Repair ERP.

This module contains static information about the application.
It is the single source of truth for product identity.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class ApplicationInfo:
    """Application metadata."""

    NAME: str = "ORM Repair ERP"

    VERSION: str = "1.0.0"

    BUILD: str = "1000"

    COMPANY: str = "Your Company Name"

    COPYRIGHT: str = "© 2026 Your Company Name"

    WEBSITE: str = "https://your-deeperp.com"

    SUPPORT_EMAIL: str = "support@your-deeperp.com"

    ENVIRONMENT: str = "Development"