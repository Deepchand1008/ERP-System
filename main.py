"""
ORM Repair ERP
Application Entry Point.
"""

from core.framework.host import ApplicationHost


def main() -> int:
    """
    Start application.
    """

    return ApplicationHost().start()


if __name__ == "__main__":

    raise SystemExit(main())