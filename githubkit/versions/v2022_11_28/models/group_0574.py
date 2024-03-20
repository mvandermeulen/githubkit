"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import Union, Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild

from .group_0357 import EnterpriseWebhooks
from .group_0358 import SimpleInstallation
from .group_0360 import RepositoryWebhooks
from .group_0361 import SimpleUserWebhooks
from .group_0359 import OrganizationSimpleWebhooks


class WebhookMemberAdded(GitHubModel):
    """member added event"""

    action: Literal["added"] = Field()
    changes: Missing[WebhookMemberAddedPropChanges] = Field(default=UNSET)
    enterprise: Missing[EnterpriseWebhooks] = Field(
        default=UNSET,
        title="Enterprise",
        description='An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured\non an enterprise account or an organization that\'s part of an enterprise account. For more information,\nsee "[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts)."\n',
    )
    installation: Missing[SimpleInstallation] = Field(
        default=UNSET,
        title="Simple Installation",
        description='The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured\nfor and sent to a GitHub App. For more information,\nsee "[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps)."',
    )
    member: Union[WebhookMemberAddedPropMember, None] = Field(title="User")
    organization: Missing[OrganizationSimpleWebhooks] = Field(
        default=UNSET,
        title="Organization Simple",
        description="A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an\norganization, or when the event occurs from activity in a repository owned by an organization.",
    )
    repository: RepositoryWebhooks = Field(
        title="Repository",
        description="The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property\nwhen the event occurs from activity in a repository.",
    )
    sender: SimpleUserWebhooks = Field(
        title="Simple User",
        description="The GitHub user that triggered the event. This property is included in every webhook payload.",
    )


class WebhookMemberAddedPropMember(GitHubModel):
    """User"""

    avatar_url: Missing[str] = Field(default=UNSET)
    deleted: Missing[bool] = Field(default=UNSET)
    email: Missing[Union[str, None]] = Field(default=UNSET)
    events_url: Missing[str] = Field(default=UNSET)
    followers_url: Missing[str] = Field(default=UNSET)
    following_url: Missing[str] = Field(default=UNSET)
    gists_url: Missing[str] = Field(default=UNSET)
    gravatar_id: Missing[str] = Field(default=UNSET)
    html_url: Missing[str] = Field(default=UNSET)
    id: int = Field()
    login: str = Field()
    name: Missing[str] = Field(default=UNSET)
    node_id: Missing[str] = Field(default=UNSET)
    organizations_url: Missing[str] = Field(default=UNSET)
    received_events_url: Missing[str] = Field(default=UNSET)
    repos_url: Missing[str] = Field(default=UNSET)
    site_admin: Missing[bool] = Field(default=UNSET)
    starred_url: Missing[str] = Field(default=UNSET)
    subscriptions_url: Missing[str] = Field(default=UNSET)
    type: Missing[Literal["Bot", "User", "Organization"]] = Field(default=UNSET)
    url: Missing[str] = Field(default=UNSET)


class WebhookMemberAddedPropChanges(GitHubModel):
    """WebhookMemberAddedPropChanges"""

    permission: Missing[WebhookMemberAddedPropChangesPropPermission] = Field(
        default=UNSET,
        description="This field is included for legacy purposes; use the `role_name` field instead. The `maintain`\nrole is mapped to `write` and the `triage` role is mapped to `read`. To determine the role\nassigned to the collaborator, use the `role_name` field instead, which will provide the full\nrole name, including custom roles.",
    )
    role_name: Missing[WebhookMemberAddedPropChangesPropRoleName] = Field(
        default=UNSET, description="The role assigned to the collaborator."
    )


class WebhookMemberAddedPropChangesPropPermission(GitHubModel):
    """WebhookMemberAddedPropChangesPropPermission

    This field is included for legacy purposes; use the `role_name` field instead.
    The `maintain`
    role is mapped to `write` and the `triage` role is mapped to `read`. To
    determine the role
    assigned to the collaborator, use the `role_name` field instead, which will
    provide the full
    role name, including custom roles.
    """

    to: Literal["write", "admin", "read"] = Field()


class WebhookMemberAddedPropChangesPropRoleName(GitHubModel):
    """WebhookMemberAddedPropChangesPropRoleName

    The role assigned to the collaborator.
    """

    to: str = Field()


model_rebuild(WebhookMemberAdded)
model_rebuild(WebhookMemberAddedPropMember)
model_rebuild(WebhookMemberAddedPropChanges)
model_rebuild(WebhookMemberAddedPropChangesPropPermission)
model_rebuild(WebhookMemberAddedPropChangesPropRoleName)

__all__ = (
    "WebhookMemberAdded",
    "WebhookMemberAddedPropMember",
    "WebhookMemberAddedPropChanges",
    "WebhookMemberAddedPropChangesPropPermission",
    "WebhookMemberAddedPropChangesPropRoleName",
)
