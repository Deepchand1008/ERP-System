"""
Application Runtime.

Maintains the runtime state of the ERP application.
"""

from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class ApplicationRuntime:
    """
    Stores the current runtime state of the application.
    """

    started_at: datetime = field(default_factory=datetime.now)

    debug: bool = True

    environment: str = "development"

    user_logged_in: bool = False

    current_user_id: int | None = None

    current_branch_id: int | None = None

    current_company_id: int | None = None

    application_ready: bool = False