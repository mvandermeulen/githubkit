"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import List

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild

from .group_0017 import Repository


class OrgsOrgActionsPermissionsRepositoriesGetResponse200(GitHubModel):
    """OrgsOrgActionsPermissionsRepositoriesGetResponse200"""

    total_count: float = Field()
    repositories: List[Repository] = Field()


model_rebuild(OrgsOrgActionsPermissionsRepositoriesGetResponse200)

__all__ = ("OrgsOrgActionsPermissionsRepositoriesGetResponse200",)
