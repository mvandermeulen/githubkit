"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing_extensions import TypedDict, NotRequired

from .group_0169 import RateLimitType


class RateLimitOverviewPropResourcesType(TypedDict):
    """RateLimitOverviewPropResources"""

    core: RateLimitType
    graphql: NotRequired[RateLimitType]
    search: RateLimitType
    code_search: NotRequired[RateLimitType]
    source_import: NotRequired[RateLimitType]
    integration_manifest: NotRequired[RateLimitType]
    code_scanning_upload: NotRequired[RateLimitType]
    actions_runner_registration: NotRequired[RateLimitType]
    scim: NotRequired[RateLimitType]
    dependency_snapshots: NotRequired[RateLimitType]


__all__ = ("RateLimitOverviewPropResourcesType",)
