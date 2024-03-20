"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from typing_extensions import TypeAlias

from ..models import WebhookSecurityAndAnalysis

Event: TypeAlias = WebhookSecurityAndAnalysis

SecurityAndAnalysisEvent: TypeAlias = Event

action_types = WebhookSecurityAndAnalysis

security_and_analysis_action_types = action_types

__all__ = (
    "Event",
    "SecurityAndAnalysisEvent",
    "action_types",
    "security_and_analysis_action_types",
)
