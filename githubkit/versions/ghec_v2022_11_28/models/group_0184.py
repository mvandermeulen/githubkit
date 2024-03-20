"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild


class ReviewCustomGatesCommentRequired(GitHubModel):
    """ReviewCustomGatesCommentRequired"""

    environment_name: str = Field(
        description="The name of the environment to approve or reject."
    )
    comment: str = Field(
        description="Comment associated with the pending deployment protection rule. **Required when state is not provided.**"
    )


model_rebuild(ReviewCustomGatesCommentRequired)

__all__ = ("ReviewCustomGatesCommentRequired",)
