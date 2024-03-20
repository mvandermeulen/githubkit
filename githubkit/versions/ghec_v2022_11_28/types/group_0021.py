"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing_extensions import TypedDict


class SimpleClassroomRepositoryType(TypedDict):
    """Simple Classroom Repository

    A GitHub repository view for Classroom
    """

    id: int
    full_name: str
    html_url: str
    node_id: str
    private: bool
    default_branch: str


__all__ = ("SimpleClassroomRepositoryType",)
