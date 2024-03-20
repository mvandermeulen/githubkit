"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import TypedDict, NotRequired

from .group_0179 import GitUserType
from .group_0180 import VerificationType


class CommitSearchResultItemPropCommitType(TypedDict):
    """CommitSearchResultItemPropCommit"""

    author: CommitSearchResultItemPropCommitPropAuthorType
    committer: Union[None, GitUserType]
    comment_count: int
    message: str
    tree: CommitSearchResultItemPropCommitPropTreeType
    url: str
    verification: NotRequired[VerificationType]


class CommitSearchResultItemPropCommitPropAuthorType(TypedDict):
    """CommitSearchResultItemPropCommitPropAuthor"""

    name: str
    email: str
    date: datetime


class CommitSearchResultItemPropCommitPropTreeType(TypedDict):
    """CommitSearchResultItemPropCommitPropTree"""

    sha: str
    url: str


__all__ = (
    "CommitSearchResultItemPropCommitType",
    "CommitSearchResultItemPropCommitPropAuthorType",
    "CommitSearchResultItemPropCommitPropTreeType",
)
