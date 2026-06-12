import uuid
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Float
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.base_class import Base


class ReadinessScore(Base):
    __tablename__ = "readiness_scores"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    ats_score = Column(Float, nullable=True, default=0)
    job_match_score = Column(Float, nullable=True, default=0)
    skill_score = Column(Float, nullable=True, default=0)
    roadmap_progress = Column(Float, nullable=True, default=0)
    interview_score = Column(Float, nullable=True, default=0)
    placement_readiness = Column(Float, nullable=True, default=0)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    user = relationship("User", back_populates="readiness_scores")
