"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import List
from typing_extensions import TypedDict

from .group_0174 import JobType


class ReposOwnerRepoActionsRunsRunIdJobsGetResponse200Type(TypedDict):
    """ReposOwnerRepoActionsRunsRunIdJobsGetResponse200"""

    total_count: int
    jobs: List[JobType]


__all__ = ("ReposOwnerRepoActionsRunsRunIdJobsGetResponse200Type",)
