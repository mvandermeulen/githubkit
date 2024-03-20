"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from datetime import datetime
from typing import Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0001 import SimpleUserType


class TimelineReviewedEventType(TypedDict):
    """Timeline Reviewed Event

    Timeline Reviewed Event
    """

    event: Literal["reviewed"]
    id: int
    node_id: str
    user: SimpleUserType
    body: Union[str, None]
    state: str
    html_url: str
    pull_request_url: str
    links: TimelineReviewedEventPropLinksType
    submitted_at: NotRequired[datetime]
    commit_id: str
    body_html: NotRequired[Union[str, None]]
    body_text: NotRequired[Union[str, None]]
    author_association: Literal[
        "COLLABORATOR",
        "CONTRIBUTOR",
        "FIRST_TIMER",
        "FIRST_TIME_CONTRIBUTOR",
        "MANNEQUIN",
        "MEMBER",
        "NONE",
        "OWNER",
    ]


class TimelineReviewedEventPropLinksType(TypedDict):
    """TimelineReviewedEventPropLinks"""

    html: TimelineReviewedEventPropLinksPropHtmlType
    pull_request: TimelineReviewedEventPropLinksPropPullRequestType


class TimelineReviewedEventPropLinksPropHtmlType(TypedDict):
    """TimelineReviewedEventPropLinksPropHtml"""

    href: str


class TimelineReviewedEventPropLinksPropPullRequestType(TypedDict):
    """TimelineReviewedEventPropLinksPropPullRequest"""

    href: str


__all__ = (
    "TimelineReviewedEventType",
    "TimelineReviewedEventPropLinksType",
    "TimelineReviewedEventPropLinksPropHtmlType",
    "TimelineReviewedEventPropLinksPropPullRequestType",
)
