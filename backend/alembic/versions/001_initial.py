"""Initial migration - create all tables

Revision ID: 001_initial
Revises:
Create Date: 2024-01-01 00:00:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision: str = "001_initial"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ── users ──────────────────────────────────────────────────────────
    op.create_table(
        "users",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True, nullable=False),
        sa.Column("email", sa.String(255), nullable=False),
        sa.Column("full_name", sa.String(255), nullable=False),
        sa.Column("hashed_password", sa.String(255), nullable=False),
        sa.Column("is_active", sa.Boolean(), nullable=False, server_default=sa.true()),
        sa.Column("target_role", sa.String(100), nullable=True),
        sa.Column("target_company", sa.String(100), nullable=True),
        sa.Column("weekly_hours", sa.String(10), nullable=True),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
        ),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=True),
    )
    op.create_index("ix_users_id", "users", ["id"])
    op.create_index("ix_users_email", "users", ["email"], unique=True)

    # ── resumes ────────────────────────────────────────────────────────
    op.create_table(
        "resumes",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True, nullable=False),
        sa.Column(
            "user_id",
            postgresql.UUID(as_uuid=True),
            sa.ForeignKey("users.id", ondelete="CASCADE"),
            nullable=False,
        ),
        sa.Column("filename", sa.String(255), nullable=False),
        sa.Column("raw_text", sa.Text(), nullable=True),
        sa.Column("ats_score", sa.Integer(), nullable=True),
        sa.Column("skills", postgresql.JSON(), nullable=True),
        sa.Column("strengths", postgresql.JSON(), nullable=True),
        sa.Column("weaknesses", postgresql.JSON(), nullable=True),
        sa.Column("recommendations", postgresql.JSON(), nullable=True),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
        ),
    )
    op.create_index("ix_resumes_id", "resumes", ["id"])
    op.create_index("ix_resumes_user_id", "resumes", ["user_id"])

    # ── job_matches ────────────────────────────────────────────────────
    op.create_table(
        "job_matches",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True, nullable=False),
        sa.Column(
            "user_id",
            postgresql.UUID(as_uuid=True),
            sa.ForeignKey("users.id", ondelete="CASCADE"),
            nullable=False,
        ),
        sa.Column("job_title", sa.String(255), nullable=True),
        sa.Column("job_description", sa.Text(), nullable=False),
        sa.Column("resume_text", sa.Text(), nullable=False),
        sa.Column("match_score", sa.Integer(), nullable=True),
        sa.Column("missing_keywords", postgresql.JSON(), nullable=True),
        sa.Column("missing_skills", postgresql.JSON(), nullable=True),
        sa.Column("improvements", postgresql.JSON(), nullable=True),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
        ),
    )
    op.create_index("ix_job_matches_id", "job_matches", ["id"])
    op.create_index("ix_job_matches_user_id", "job_matches", ["user_id"])

    # ── roadmaps ───────────────────────────────────────────────────────
    op.create_table(
        "roadmaps",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True, nullable=False),
        sa.Column(
            "user_id",
            postgresql.UUID(as_uuid=True),
            sa.ForeignKey("users.id", ondelete="CASCADE"),
            nullable=False,
        ),
        sa.Column("target_role", sa.String(100), nullable=False),
        sa.Column("target_company", sa.String(100), nullable=True),
        sa.Column("weekly_hours", sa.Integer(), nullable=False, server_default="10"),
        sa.Column("current_skills", postgresql.JSON(), nullable=True),
        sa.Column("weeks", postgresql.JSON(), nullable=True),
        sa.Column("total_weeks", sa.Integer(), nullable=True),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
        ),
    )
    op.create_index("ix_roadmaps_id", "roadmaps", ["id"])
    op.create_index("ix_roadmaps_user_id", "roadmaps", ["user_id"])

    # ── interview_sessions ─────────────────────────────────────────────
    op.create_table(
        "interview_sessions",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True, nullable=False),
        sa.Column(
            "user_id",
            postgresql.UUID(as_uuid=True),
            sa.ForeignKey("users.id", ondelete="CASCADE"),
            nullable=False,
        ),
        sa.Column("company", sa.String(100), nullable=True),
        sa.Column("role", sa.String(100), nullable=True),
        sa.Column("question", sa.Text(), nullable=False),
        sa.Column("answer", sa.Text(), nullable=False),
        sa.Column("technical_score", sa.Float(), nullable=True),
        sa.Column("communication_score", sa.Float(), nullable=True),
        sa.Column("confidence_score", sa.Float(), nullable=True),
        sa.Column("feedback", postgresql.JSON(), nullable=True),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
        ),
    )
    op.create_index("ix_interview_sessions_id", "interview_sessions", ["id"])
    op.create_index("ix_interview_sessions_user_id", "interview_sessions", ["user_id"])

    # ── readiness_scores ───────────────────────────────────────────────
    op.create_table(
        "readiness_scores",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True, nullable=False),
        sa.Column(
            "user_id",
            postgresql.UUID(as_uuid=True),
            sa.ForeignKey("users.id", ondelete="CASCADE"),
            nullable=False,
        ),
        sa.Column("ats_score", sa.Float(), nullable=True, server_default="0"),
        sa.Column("job_match_score", sa.Float(), nullable=True, server_default="0"),
        sa.Column("skill_score", sa.Float(), nullable=True, server_default="0"),
        sa.Column("roadmap_progress", sa.Float(), nullable=True, server_default="0"),
        sa.Column("interview_score", sa.Float(), nullable=True, server_default="0"),
        sa.Column("placement_readiness", sa.Float(), nullable=True, server_default="0"),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
        ),
    )
    op.create_index("ix_readiness_scores_id", "readiness_scores", ["id"])
    op.create_index("ix_readiness_scores_user_id", "readiness_scores", ["user_id"])


def downgrade() -> None:
    op.drop_table("readiness_scores")
    op.drop_table("interview_sessions")
    op.drop_table("roadmaps")
    op.drop_table("job_matches")
    op.drop_table("resumes")
    op.drop_table("users")
