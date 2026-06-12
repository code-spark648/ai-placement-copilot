"""
Centralized dependency injection for FastAPI routes.
Import from here to keep routes clean.
"""

from typing import Generator
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.session import SessionLocal, get_db
from app.core.security import get_current_user
from app.models.user import User


def get_active_user(current_user: User = Depends(get_current_user)) -> User:
    """Return current user, raising 403 if account is inactive."""
    if not current_user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Your account has been deactivated. Please contact support.",
        )
    return current_user


def paginate(skip: int = 0, limit: int = 20):
    """Reusable pagination dependency."""
    if limit > 100:
        limit = 100
    return {"skip": skip, "limit": limit}
