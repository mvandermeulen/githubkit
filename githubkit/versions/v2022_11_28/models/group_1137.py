"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import Literal

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild


class UserMembershipsOrgsOrgPatchBody(GitHubModel):
    """UserMembershipsOrgsOrgPatchBody"""

    state: Literal["active"] = Field(
        description='The state that the membership should be in. Only `"active"` will be accepted.'
    )


model_rebuild(UserMembershipsOrgsOrgPatchBody)

__all__ = ("UserMembershipsOrgsOrgPatchBody",)
