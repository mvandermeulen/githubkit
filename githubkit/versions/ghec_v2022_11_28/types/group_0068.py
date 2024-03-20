"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import TypedDict, NotRequired

from .group_0001 import SimpleUserType


class GistCommitType(TypedDict):
    """Gist Commit

    Gist Commit
    """

    url: str
    version: str
    user: Union[None, SimpleUserType]
    change_status: GistCommitPropChangeStatusType
    committed_at: datetime


class GistCommitPropChangeStatusType(TypedDict):
    """GistCommitPropChangeStatus"""

    total: NotRequired[int]
    additions: NotRequired[int]
    deletions: NotRequired[int]


__all__ = (
    "GistCommitType",
    "GistCommitPropChangeStatusType",
)
