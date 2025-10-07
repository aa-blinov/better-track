"""Configuration management."""

from pathlib import Path

# Default paths
DATA_DIR = Path.home() / ".track"
DB_PATH = DATA_DIR / "track.db"

# Ensure data directory exists
DATA_DIR.mkdir(parents=True, exist_ok=True)
