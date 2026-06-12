"""
Database initialization utility.
Run this script to create all tables directly (alternative to Alembic for development).

Usage:
    python -m app.db.init_db
"""

import logging
from sqlalchemy import text
from app.db.session import engine
from app.db.base_class import Base

# Import all models so SQLAlchemy registers them before create_all
from app.models.user import User  # noqa
from app.models.resume import Resume  # noqa
from app.models.job_match import JobMatch  # noqa
from app.models.roadmap import Roadmap  # noqa
from app.models.interview import InterviewSession  # noqa
from app.models.readiness import ReadinessScore  # noqa

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def init_db() -> None:
    logger.info("Creating database tables...")
    Base.metadata.create_all(bind=engine)
    logger.info("All tables created successfully.")

    # Verify connection
    with engine.connect() as conn:
        result = conn.execute(text("SELECT 1"))
        logger.info(f"Database connection verified: {result.fetchone()}")


if __name__ == "__main__":
    init_db()
