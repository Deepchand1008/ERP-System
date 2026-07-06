from core.framework.exceptions import (
    ExceptionHandler,
    ValidationException,
)

try:
    raise ValidationException("Customer name is required.")
except Exception as exc:
    ExceptionHandler.handle(exc)