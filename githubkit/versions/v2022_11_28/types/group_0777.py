"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from datetime import datetime
from typing import List, Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0351 import EnterpriseWebhooksType
from .group_0352 import SimpleInstallationType
from .group_0355 import SimpleUserWebhooksType
from .group_0353 import OrganizationSimpleWebhooksType


class WebhookTeamAddedToRepositoryType(TypedDict):
    """team added_to_repository event"""

    action: Literal["added_to_repository"]
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: OrganizationSimpleWebhooksType
    repository: NotRequired[WebhookTeamAddedToRepositoryPropRepositoryType]
    sender: NotRequired[SimpleUserWebhooksType]
    team: WebhookTeamAddedToRepositoryPropTeamType


class WebhookTeamAddedToRepositoryPropRepositoryType(TypedDict):
    """Repository

    A git repository
    """

    allow_auto_merge: NotRequired[bool]
    allow_forking: NotRequired[bool]
    allow_merge_commit: NotRequired[bool]
    allow_rebase_merge: NotRequired[bool]
    allow_squash_merge: NotRequired[bool]
    allow_update_branch: NotRequired[bool]
    archive_url: str
    archived: bool
    assignees_url: str
    blobs_url: str
    branches_url: str
    clone_url: str
    collaborators_url: str
    comments_url: str
    commits_url: str
    compare_url: str
    contents_url: str
    contributors_url: str
    created_at: Union[int, datetime]
    custom_properties: NotRequired[
        WebhookTeamAddedToRepositoryPropRepositoryPropCustomPropertiesType
    ]
    default_branch: str
    delete_branch_on_merge: NotRequired[bool]
    deployments_url: str
    description: Union[str, None]
    disabled: NotRequired[bool]
    downloads_url: str
    events_url: str
    fork: bool
    forks: int
    forks_count: int
    forks_url: str
    full_name: str
    git_commits_url: str
    git_refs_url: str
    git_tags_url: str
    git_url: str
    has_downloads: bool
    has_issues: bool
    has_pages: bool
    has_projects: bool
    has_wiki: bool
    homepage: Union[str, None]
    hooks_url: str
    html_url: str
    id: int
    is_template: NotRequired[bool]
    issue_comment_url: str
    issue_events_url: str
    issues_url: str
    keys_url: str
    labels_url: str
    language: Union[str, None]
    languages_url: str
    license_: Union[WebhookTeamAddedToRepositoryPropRepositoryPropLicenseType, None]
    master_branch: NotRequired[str]
    merges_url: str
    milestones_url: str
    mirror_url: Union[str, None]
    name: str
    node_id: str
    notifications_url: str
    open_issues: int
    open_issues_count: int
    organization: NotRequired[str]
    owner: Union[WebhookTeamAddedToRepositoryPropRepositoryPropOwnerType, None]
    permissions: NotRequired[
        WebhookTeamAddedToRepositoryPropRepositoryPropPermissionsType
    ]
    private: bool
    public: NotRequired[bool]
    pulls_url: str
    pushed_at: Union[int, datetime, None]
    releases_url: str
    role_name: NotRequired[Union[str, None]]
    size: int
    ssh_url: str
    stargazers: NotRequired[int]
    stargazers_count: int
    stargazers_url: str
    statuses_url: str
    subscribers_url: str
    subscription_url: str
    svn_url: str
    tags_url: str
    teams_url: str
    topics: List[str]
    trees_url: str
    updated_at: datetime
    url: str
    visibility: Literal["public", "private", "internal"]
    watchers: int
    watchers_count: int


class WebhookTeamAddedToRepositoryPropRepositoryPropCustomPropertiesType(TypedDict):
    """WebhookTeamAddedToRepositoryPropRepositoryPropCustomProperties

    The custom properties that were defined for the repository. The keys are the
    custom property names, and the values are the corresponding custom property
    values.
    """


class WebhookTeamAddedToRepositoryPropRepositoryPropLicenseType(TypedDict):
    """License"""

    key: str
    name: str
    node_id: str
    spdx_id: str
    url: Union[str, None]


class WebhookTeamAddedToRepositoryPropRepositoryPropOwnerType(TypedDict):
    """User"""

    avatar_url: NotRequired[str]
    deleted: NotRequired[bool]
    email: NotRequired[Union[str, None]]
    events_url: NotRequired[str]
    followers_url: NotRequired[str]
    following_url: NotRequired[str]
    gists_url: NotRequired[str]
    gravatar_id: NotRequired[str]
    html_url: NotRequired[str]
    id: int
    login: str
    name: NotRequired[str]
    node_id: NotRequired[str]
    organizations_url: NotRequired[str]
    received_events_url: NotRequired[str]
    repos_url: NotRequired[str]
    site_admin: NotRequired[bool]
    starred_url: NotRequired[str]
    subscriptions_url: NotRequired[str]
    type: NotRequired[Literal["Bot", "User", "Organization"]]
    url: NotRequired[str]


class WebhookTeamAddedToRepositoryPropRepositoryPropPermissionsType(TypedDict):
    """WebhookTeamAddedToRepositoryPropRepositoryPropPermissions"""

    admin: bool
    maintain: NotRequired[bool]
    pull: bool
    push: bool
    triage: NotRequired[bool]


class WebhookTeamAddedToRepositoryPropTeamType(TypedDict):
    """Team

    Groups of organization members that gives permissions on specified repositories.
    """

    deleted: NotRequired[bool]
    description: NotRequired[Union[str, None]]
    html_url: NotRequired[str]
    id: int
    members_url: NotRequired[str]
    name: str
    node_id: NotRequired[str]
    parent: NotRequired[Union[WebhookTeamAddedToRepositoryPropTeamPropParentType, None]]
    permission: NotRequired[str]
    privacy: NotRequired[Literal["open", "closed", "secret"]]
    notification_setting: NotRequired[
        Literal["notifications_enabled", "notifications_disabled"]
    ]
    repositories_url: NotRequired[str]
    slug: NotRequired[str]
    url: NotRequired[str]


class WebhookTeamAddedToRepositoryPropTeamPropParentType(TypedDict):
    """WebhookTeamAddedToRepositoryPropTeamPropParent"""

    description: Union[str, None]
    html_url: str
    id: int
    members_url: str
    name: str
    node_id: str
    permission: str
    privacy: Literal["open", "closed", "secret"]
    notification_setting: Literal["notifications_enabled", "notifications_disabled"]
    repositories_url: str
    slug: str
    url: str


__all__ = (
    "WebhookTeamAddedToRepositoryType",
    "WebhookTeamAddedToRepositoryPropRepositoryType",
    "WebhookTeamAddedToRepositoryPropRepositoryPropCustomPropertiesType",
    "WebhookTeamAddedToRepositoryPropRepositoryPropLicenseType",
    "WebhookTeamAddedToRepositoryPropRepositoryPropOwnerType",
    "WebhookTeamAddedToRepositoryPropRepositoryPropPermissionsType",
    "WebhookTeamAddedToRepositoryPropTeamType",
    "WebhookTeamAddedToRepositoryPropTeamPropParentType",
)