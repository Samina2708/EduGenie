"""Workspace-root ASGI entrypoint for the EduGenie application."""

from pathlib import Path
import sys


APP_DIR = Path(__file__).resolve().parent / "EduGenie"
if str(APP_DIR) not in sys.path:
    sys.path.insert(0, str(APP_DIR))

from EduGenie.main import app

__all__ = ["app"]