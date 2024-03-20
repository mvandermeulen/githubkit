"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from datetime import datetime
from typing import Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0755 import (
    WebhookRepositoryVulnerabilityAlertResolvePropAlertAllof0PropDismisserType,
)


class WebhookRepositoryVulnerabilityAlertResolvePropAlertType(TypedDict):
    """WebhookRepositoryVulnerabilityAlertResolvePropAlert"""

    affected_package_name: str
    affected_range: str
    created_at: str
    dismiss_reason: NotRequired[str]
    dismissed_at: NotRequired[str]
    dismisser: NotRequired[
        Union[
            WebhookRepositoryVulnerabilityAlertResolvePropAlertAllof0PropDismisserType,
            None,
        ]
    ]
    external_identifier: str
    external_reference: Union[Union[str, None], None]
    fix_reason: NotRequired[str]
    fixed_at: NotRequired[datetime]
    fixed_in: NotRequired[str]
    ghsa_id: str
    id: int
    node_id: str
    number: int
    severity: str
    state: Literal["fixed", "open"]


__all__ = ("WebhookRepositoryVulnerabilityAlertResolvePropAlertType",)
