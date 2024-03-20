"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from datetime import datetime
from typing import Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0090 import TeamType
from .group_0060 import IssueType
from .group_0001 import SimpleUserType
from .group_0005 import IntegrationType


class IssueEventType(TypedDict):
    """Issue Event

    Issue Event
    """

    id: int
    node_id: str
    url: str
    actor: Union[None, SimpleUserType]
    event: str
    commit_id: Union[str, None]
    commit_url: Union[str, None]
    created_at: datetime
    issue: NotRequired[Union[None, IssueType]]
    label: NotRequired[IssueEventLabelType]
    assignee: NotRequired[Union[None, SimpleUserType]]
    assigner: NotRequired[Union[None, SimpleUserType]]
    review_requester: NotRequired[Union[None, SimpleUserType]]
    requested_reviewer: NotRequired[Union[None, SimpleUserType]]
    requested_team: NotRequired[TeamType]
    dismissed_review: NotRequired[IssueEventDismissedReviewType]
    milestone: NotRequired[IssueEventMilestoneType]
    project_card: NotRequired[IssueEventProjectCardType]
    rename: NotRequired[IssueEventRenameType]
    author_association: NotRequired[
        Literal[
            "COLLABORATOR",
            "CONTRIBUTOR",
            "FIRST_TIMER",
            "FIRST_TIME_CONTRIBUTOR",
            "MANNEQUIN",
            "MEMBER",
            "NONE",
            "OWNER",
        ]
    ]
    lock_reason: NotRequired[Union[str, None]]
    performed_via_github_app: NotRequired[Union[None, IntegrationType]]


class IssueEventLabelType(TypedDict):
    """Issue Event Label

    Issue Event Label
    """

    name: Union[str, None]
    color: Union[str, None]


class IssueEventDismissedReviewType(TypedDict):
    """Issue Event Dismissed Review"""

    state: str
    review_id: int
    dismissal_message: Union[str, None]
    dismissal_commit_id: NotRequired[Union[str, None]]


class IssueEventMilestoneType(TypedDict):
    """Issue Event Milestone

    Issue Event Milestone
    """

    title: str


class IssueEventProjectCardType(TypedDict):
    """Issue Event Project Card

    Issue Event Project Card
    """

    url: str
    id: int
    project_url: str
    project_id: int
    column_name: str
    previous_column_name: NotRequired[str]


class IssueEventRenameType(TypedDict):
    """Issue Event Rename

    Issue Event Rename
    """

    from_: str
    to: str


__all__ = (
    "IssueEventType",
    "IssueEventLabelType",
    "IssueEventDismissedReviewType",
    "IssueEventMilestoneType",
    "IssueEventProjectCardType",
    "IssueEventRenameType",
)
