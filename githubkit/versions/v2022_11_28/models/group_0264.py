"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import Union, Literal

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild

from .group_0001 import SimpleUser
from .group_0005 import Integration


class LockedIssueEvent(GitHubModel):
    """Locked Issue Event

    Locked Issue Event
    """

    id: int = Field()
    node_id: str = Field()
    url: str = Field()
    actor: SimpleUser = Field(title="Simple User", description="A GitHub user.")
    event: Literal["locked"] = Field()
    commit_id: Union[str, None] = Field()
    commit_url: Union[str, None] = Field()
    created_at: str = Field()
    performed_via_github_app: Union[None, Integration] = Field()
    lock_reason: Union[str, None] = Field()


model_rebuild(LockedIssueEvent)

__all__ = ("LockedIssueEvent",)
