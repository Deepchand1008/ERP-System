"""
Application Settings Model.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class SettingsModel:
    """Application settings."""

    theme: str = "light"

    language: str = "en"

    timezone: str = "Asia/Kolkata"

    currency: str = "INR"

    date_format: str = "%d-%m-%Y"

    time_format: str = "%H:%M"

    company_name: str = "ORM Repair ERP"

    company_address: str = ""

    company_phone: str = ""

    company_email: str = ""

    default_printer: str = ""