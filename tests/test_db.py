"""Database tests."""

from datetime import datetime

import pytest

from track.db import Database


@pytest.fixture
def temp_db():
    """Create temporary database for testing."""
    # Use in-memory database for tests
    db = Database(":memory:")
    yield db
    db.close()


def test_create_activity(temp_db):
    """Test activity creation."""
    activity = temp_db.create_activity("reading")
    assert activity.id is not None
    assert activity.name == "reading"
    assert activity.archived is False


def test_get_or_create_activity(temp_db):
    """Test get or create activity."""
    activity1 = temp_db.get_or_create_activity("reading")
    activity2 = temp_db.get_or_create_activity("reading")
    assert activity1.id == activity2.id


def test_create_session(temp_db):
    """Test session creation."""
    activity = temp_db.create_activity("reading")
    start = datetime.now()
    session = temp_db.create_session(activity.id, start)

    assert session.id is not None
    assert session.activity_id == activity.id
    assert session.start_at == start
    assert session.end_at is None


def test_active_sessions(temp_db):
    """Test getting active sessions."""
    activity = temp_db.create_activity("reading")
    session = temp_db.create_session(activity.id, datetime.now())

    active = temp_db.get_active_sessions()
    assert len(active) == 1
    assert active[0][0].id == session.id
    assert active[0][1].name == "reading"


def test_stop_session(temp_db):
    """Test stopping a session."""
    activity = temp_db.create_activity("reading")
    session = temp_db.create_session(activity.id, datetime.now())

    end = datetime.now()
    temp_db.update_session(session.id, end_at=end)

    updated = temp_db.get_session(session.id)
    assert updated.end_at is not None

    active = temp_db.get_active_sessions()
    assert len(active) == 0


def test_tags(temp_db):
    """Test tag operations."""
    tag1 = temp_db.get_or_create_tag("work")
    tag2 = temp_db.get_or_create_tag("work")
    assert tag1.id == tag2.id

    activity = temp_db.create_activity("coding")
    session = temp_db.create_session(activity.id, datetime.now())

    temp_db.add_session_tag(session.id, tag1.id)
    tags = temp_db.get_session_tags(session.id)
    assert len(tags) == 1
    assert tags[0].name == "work"
