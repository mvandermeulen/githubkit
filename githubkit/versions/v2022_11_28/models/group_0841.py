"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild


class OrgsOrgActionsPermissionsPutBody(GitHubModel):
    """OrgsOrgActionsPermissionsPutBody"""

    enabled_repositories: Literal["all", "none", "selected"] = Field(
        description="The policy that controls the repositories in the organization that are allowed to run GitHub Actions."
    )
    allowed_actions: Missing[Literal["all", "local_only", "selected"]] = Field(
        default=UNSET,
        description="The permissions policy that controls the actions and reusable workflows that are allowed to run.",
    )


model_rebuild(OrgsOrgActionsPermissionsPutBody)

__all__ = ("OrgsOrgActionsPermissionsPutBody",)
