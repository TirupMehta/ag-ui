"""AG-UI integration for Google Antigravity."""

from .agent import AntigravityAgent
from .endpoint import add_antigravity_fastapi_endpoint, create_antigravity_app
from .event_translator import EventTranslator
from .session_manager import (
    AntigravitySession,
    SessionLimitExceeded,
    SessionManager,
)
from .ui_bridge import (
    InterruptAnswer,
    UIBridge,
    get_context,
    get_state,
    interrupt,
    set_state,
)

__all__ = [
    "AntigravityAgent",
    "AntigravitySession",
    "EventTranslator",
    "SessionLimitExceeded",
    "SessionManager",
    "UIBridge",
    "add_antigravity_fastapi_endpoint",
    "create_antigravity_app",
    "InterruptAnswer",
    "get_context",
    "interrupt",
    "get_state",
    "set_state",
]

__version__ = "0.1.0"
