"""
Application Settings Manager.
"""

from .settings_model import SettingsModel


class SettingsManager:
    """
    Manages application settings.

    Later this class can load settings from:
    - REST API
    - Local cache
    - PostgreSQL
    """

    def __init__(self) -> None:
        self._settings = SettingsModel()

    @property
    def settings(self) -> SettingsModel:
        return self._settings

    def load(self) -> None:
        """
        Load application settings.

        Placeholder for future implementation.
        """
        pass