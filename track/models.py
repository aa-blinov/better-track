"""Data models."""

from dataclasses import dataclass
from datetime import datetime


@dataclass
class Activity:
    """Activity model."""

    id: int | None
    name: str
    archived: bool = False
    created_at: datetime | None = None
    updated_at: datetime | None = None


@dataclass
class Session:
    """Session model."""

    id: int | None
    activity_id: int
    start_at: datetime
    end_at: datetime | None = None
    note: str | None = None
    paused: bool = False
    paused_at: datetime | None = None
    accumulated_seconds: int = 0
    last_resume_at: datetime | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None


@dataclass
class Tag:
    """Tag model."""

    id: int | None
    name: str
    created_at: datetime | None = None


@dataclass
class SessionTag:
    """Session-Tag relationship."""

    session_id: int
    tag_id: int


@dataclass
class Goal:
    """Goal model."""

    id: int | None
    activity_id: int
    period: str  # daily, weekly, monthly
    target_minutes: int
    created_at: datetime | None = None
    updated_at: datetime | None = None


@dataclass
class Reminder:
    """Reminder model."""

    id: int | None
    activity_id: int
    every_minutes: int
    window: str | None = None  # e.g., "09:00-18:00"
    enabled: bool = True
    created_at: datetime | None = None
    updated_at: datetime | None = None
