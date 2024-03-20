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

from .group_0119 import RepositoryRuleCommitMessagePatternPropParameters


class RepositoryRuleCommitMessagePattern(GitHubModel):
    """commit_message_pattern

    Parameters to be used for the commit_message_pattern rule
    """

    type: Literal["commit_message_pattern"] = Field()
    parameters: Missing[RepositoryRuleCommitMessagePatternPropParameters] = Field(
        default=UNSET
    )


model_rebuild(RepositoryRuleCommitMessagePattern)

__all__ = ("RepositoryRuleCommitMessagePattern",)
