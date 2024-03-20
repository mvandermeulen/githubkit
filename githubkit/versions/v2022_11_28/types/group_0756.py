"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from datetime import datetime
from typing import Union, Literal
from typing_extensions import TypedDict, NotRequired


class WebhookRepositoryVulnerabilityAlertResolvePropAlertAllof1Type(TypedDict):
    """WebhookRepositoryVulnerabilityAlertResolvePropAlertAllof1"""

    affected_package_name: NotRequired[str]
    affected_range: NotRequired[str]
    created_at: NotRequired[str]
    external_identifier: NotRequired[str]
    external_reference: NotRequired[Union[str, None]]
    fix_reason: NotRequired[str]
    fixed_at: NotRequired[datetime]
    fixed_in: NotRequired[str]
    ghsa_id: NotRequired[str]
    id: NotRequired[int]
    node_id: NotRequired[str]
    number: NotRequired[int]
    severity: NotRequired[str]
    state: Literal["fixed", "open"]


__all__ = ("WebhookRepositoryVulnerabilityAlertResolvePropAlertAllof1Type",)
