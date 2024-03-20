"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from datetime import datetime
from typing import Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0001 import SimpleUserType


class SecretScanningAlertType(TypedDict):
    """SecretScanningAlert"""

    number: NotRequired[int]
    created_at: NotRequired[datetime]
    updated_at: NotRequired[Union[None, datetime]]
    url: NotRequired[str]
    html_url: NotRequired[str]
    locations_url: NotRequired[str]
    state: NotRequired[Literal["open", "resolved"]]
    resolution: NotRequired[
        Union[None, Literal["false_positive", "wont_fix", "revoked", "used_in_tests"]]
    ]
    resolved_at: NotRequired[Union[datetime, None]]
    resolved_by: NotRequired[Union[None, SimpleUserType]]
    resolution_comment: NotRequired[Union[str, None]]
    secret_type: NotRequired[str]
    secret_type_display_name: NotRequired[str]
    secret: NotRequired[str]
    push_protection_bypassed: NotRequired[Union[bool, None]]
    push_protection_bypassed_by: NotRequired[Union[None, SimpleUserType]]
    push_protection_bypassed_at: NotRequired[Union[datetime, None]]
    validity: NotRequired[Literal["active", "inactive", "unknown"]]


__all__ = ("SecretScanningAlertType",)
