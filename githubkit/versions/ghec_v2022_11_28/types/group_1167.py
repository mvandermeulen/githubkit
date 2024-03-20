"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import List
from typing_extensions import TypedDict, NotRequired


class ScimV2OrganizationsOrgUsersScimUserIdPutBodyType(TypedDict):
    """ScimV2OrganizationsOrgUsersScimUserIdPutBody"""

    schemas: NotRequired[List[str]]
    display_name: NotRequired[str]
    external_id: NotRequired[str]
    groups: NotRequired[List[str]]
    active: NotRequired[bool]
    user_name: str
    name: ScimV2OrganizationsOrgUsersScimUserIdPutBodyPropNameType
    emails: List[ScimV2OrganizationsOrgUsersScimUserIdPutBodyPropEmailsItemsType]


class ScimV2OrganizationsOrgUsersScimUserIdPutBodyPropNameType(TypedDict):
    """ScimV2OrganizationsOrgUsersScimUserIdPutBodyPropName

    Examples:
        {'givenName': 'Jane', 'familyName': 'User'}
    """

    given_name: str
    family_name: str
    formatted: NotRequired[str]


class ScimV2OrganizationsOrgUsersScimUserIdPutBodyPropEmailsItemsType(TypedDict):
    """ScimV2OrganizationsOrgUsersScimUserIdPutBodyPropEmailsItems"""

    type: NotRequired[str]
    value: str
    primary: NotRequired[bool]


__all__ = (
    "ScimV2OrganizationsOrgUsersScimUserIdPutBodyType",
    "ScimV2OrganizationsOrgUsersScimUserIdPutBodyPropNameType",
    "ScimV2OrganizationsOrgUsersScimUserIdPutBodyPropEmailsItemsType",
)
