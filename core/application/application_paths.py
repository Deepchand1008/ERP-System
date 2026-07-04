"""
Application path manager.

Provides centralized access to all project directories.
"""

from pathlib import Path


class ApplicationPaths:
    """Centralized project paths."""

    # Project Root

    ROOT = Path(__file__).resolve().parents[2]

    # Config

    CONFIG = ROOT / "config"

    # Resources

    RESOURCES = ROOT / "resources"

    ICONS = RESOURCES / "icons"

    IMAGES = RESOURCES / "images"

    THEMES = RESOURCES / "qss"

    FONTS = RESOURCES / "fonts"

    # Storage

    STORAGE = ROOT / "storage"

    LOGS = STORAGE / "logs"

    CACHE = STORAGE / "cache"

    BACKUPS = STORAGE / "backups"

    EXPORTS = STORAGE / "exports"

    IMPORTS = STORAGE / "imports"

    TEMP = STORAGE / "temp"

    REPORTS = STORAGE / "reports"

    # Documentation

    DOCS = ROOT / "docs"

    # Tests

    TESTS = ROOT / "tests"