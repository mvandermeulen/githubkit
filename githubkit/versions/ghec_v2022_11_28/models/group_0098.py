"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import List

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild


class ExternalGroups(GitHubModel):
    """ExternalGroups

    A list of external groups available to be connected to a team
    """

    groups: Missing[List[ExternalGroupsPropGroupsItems]] = Field(
        default=UNSET,
        description="An array of external groups available to be mapped to a team",
    )


class ExternalGroupsPropGroupsItems(GitHubModel):
    """ExternalGroupsPropGroupsItems"""

    group_id: int = Field(description="The internal ID of the group")
    group_name: str = Field(description="The display name of the group")
    updated_at: str = Field(description="The time of the last update for this group")


model_rebuild(ExternalGroups)
model_rebuild(ExternalGroupsPropGroupsItems)

__all__ = (
    "ExternalGroups",
    "ExternalGroupsPropGroupsItems",
)
