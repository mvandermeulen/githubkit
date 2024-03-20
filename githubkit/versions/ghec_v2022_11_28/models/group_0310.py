"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import Union

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild

from .group_0311 import PullRequestPropBasePropRepo


class PullRequestPropBase(GitHubModel):
    """PullRequestPropBase"""

    label: str = Field()
    ref: str = Field()
    repo: PullRequestPropBasePropRepo = Field()
    sha: str = Field()
    user: PullRequestPropBasePropUser = Field()


class PullRequestPropBasePropUser(GitHubModel):
    """PullRequestPropBasePropUser"""

    avatar_url: str = Field()
    events_url: str = Field()
    followers_url: str = Field()
    following_url: str = Field()
    gists_url: str = Field()
    gravatar_id: Union[str, None] = Field()
    html_url: str = Field()
    id: int = Field()
    node_id: str = Field()
    login: str = Field()
    organizations_url: str = Field()
    received_events_url: str = Field()
    repos_url: str = Field()
    site_admin: bool = Field()
    starred_url: str = Field()
    subscriptions_url: str = Field()
    type: str = Field()
    url: str = Field()


model_rebuild(PullRequestPropBase)
model_rebuild(PullRequestPropBasePropUser)

__all__ = (
    "PullRequestPropBase",
    "PullRequestPropBasePropUser",
)
