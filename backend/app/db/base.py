"""
Import this module anywhere you need Alembic/SQLAlchemy to see all models.
It simply re-exports Base and imports every model once so metadata is populated.
"""

from app.db.base_class import Base  # noqa: F401

# Model imports — order matters: User first (no FK deps), then dependents
from app.models.user import User  # noqa: F401
from app.models.resume import Resume  # noqa: F401
from app.models.job_match import JobMatch  # noqa: F401
from app.models.roadmap import Roadmap  # noqa: F401
from app.models.interview import InterviewSession  # noqa: F401
from app.models.readiness import ReadinessScore  # noqa: F401
