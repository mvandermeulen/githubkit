"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List
from typing_extensions import TypedDict, NotRequired


class AdvancedSecurityActiveCommittersType(TypedDict):
    """AdvancedSecurityActiveCommitters"""

    total_advanced_security_committers: NotRequired[int]
    total_count: NotRequired[int]
    maximum_advanced_security_committers: NotRequired[int]
    purchased_advanced_security_committers: NotRequired[int]
    repositories: List[AdvancedSecurityActiveCommittersRepositoryType]


class AdvancedSecurityActiveCommittersRepositoryType(TypedDict):
    """AdvancedSecurityActiveCommittersRepository"""

    name: str
    advanced_security_committers: int
    advanced_security_committers_breakdown: List[
        AdvancedSecurityActiveCommittersUserType
    ]


class AdvancedSecurityActiveCommittersUserType(TypedDict):
    """AdvancedSecurityActiveCommittersUser"""

    user_login: str
    last_pushed_date: str
    last_pushed_email: str


__all__ = (
    "AdvancedSecurityActiveCommittersType",
    "AdvancedSecurityActiveCommittersRepositoryType",
    "AdvancedSecurityActiveCommittersUserType",
)