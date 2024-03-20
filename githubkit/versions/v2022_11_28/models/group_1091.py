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


class ReposOwnerRepoPullsPullNumberUpdateBranchPutBody(GitHubModel):
    """ReposOwnerRepoPullsPullNumberUpdateBranchPutBody"""

    expected_head_sha: Missing[str] = Field(
        default=UNSET,
        description="The expected SHA of the pull request's HEAD ref. This is the most recent commit on the pull request's branch. If the expected SHA does not match the pull request's HEAD, you will receive a `422 Unprocessable Entity` status. You can use the \"[List commits](https://docs.github.com/rest/commits/commits#list-commits)\" endpoint to find the most recent commit SHA. Default: SHA of the pull request's current HEAD ref.",
    )


model_rebuild(ReposOwnerRepoPullsPullNumberUpdateBranchPutBody)

__all__ = ("ReposOwnerRepoPullsPullNumberUpdateBranchPutBody",)
