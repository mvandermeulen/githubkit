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


class ReposOwnerRepoActionsJobsJobIdRerunPostBody(GitHubModel):
    """ReposOwnerRepoActionsJobsJobIdRerunPostBody"""

    enable_debug_logging: Missing[bool] = Field(
        default=UNSET, description="Whether to enable debug logging for the re-run."
    )


model_rebuild(ReposOwnerRepoActionsJobsJobIdRerunPostBody)

__all__ = ("ReposOwnerRepoActionsJobsJobIdRerunPostBody",)
