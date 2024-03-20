"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from datetime import datetime
from typing import Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0745 import (
    WebhookRepositoryVulnerabilityAlertDismissPropAlertAllof0PropDismisserType,
)


class WebhookRepositoryVulnerabilityAlertDismissPropAlertType(TypedDict):
    """WebhookRepositoryVulnerabilityAlertDismissPropAlert"""

    affected_package_name: str
    affected_range: str
    created_at: str
    dismiss_comment: NotRequired[Union[Union[str, None], None]]
    dismiss_reason: str
    dismissed_at: str
    dismisser: Union[
        Union[
            WebhookRepositoryVulnerabilityAlertDismissPropAlertAllof0PropDismisserType,
            None,
        ],
        None,
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
    state: Literal["dismissed"]


__all__ = ("WebhookRepositoryVulnerabilityAlertDismissPropAlertType",)
