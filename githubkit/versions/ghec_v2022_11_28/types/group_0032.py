"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import TypedDict, NotRequired


class ActionsSetDefaultWorkflowPermissionsType(TypedDict):
    """ActionsSetDefaultWorkflowPermissions"""

    default_workflow_permissions: NotRequired[Literal["read", "write"]]
    can_approve_pull_request_reviews: NotRequired[bool]


__all__ = ("ActionsSetDefaultWorkflowPermissionsType",)