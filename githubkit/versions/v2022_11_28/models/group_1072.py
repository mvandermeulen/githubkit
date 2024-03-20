"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild


class ReposOwnerRepoProjectsPostBody(GitHubModel):
    """ReposOwnerRepoProjectsPostBody"""

    name: str = Field(description="The name of the project.")
    body: Missing[str] = Field(
        default=UNSET, description="The description of the project."
    )


model_rebuild(ReposOwnerRepoProjectsPostBody)

__all__ = ("ReposOwnerRepoProjectsPostBody",)
