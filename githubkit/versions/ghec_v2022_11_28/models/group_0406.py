"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from datetime import datetime
from typing import List, Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild

from .group_0390 import EnterpriseWebhooks
from .group_0391 import SimpleInstallation
from .group_0393 import RepositoryWebhooks
from .group_0394 import SimpleUserWebhooks
from .group_0392 import OrganizationSimpleWebhooks


class WebhookBranchProtectionRuleDeleted(GitHubModel):
    """branch protection rule deleted event"""

    action: Literal["deleted"] = Field()
    enterprise: Missing[EnterpriseWebhooks] = Field(
        default=UNSET,
        title="Enterprise",
        description='An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured\non an enterprise account or an organization that\'s part of an enterprise account. For more information,\nsee "[About enterprise accounts](https://docs.github.com/enterprise-cloud@latest//admin/overview/about-enterprise-accounts)."\n',
    )
    installation: Missing[SimpleInstallation] = Field(
        default=UNSET,
        title="Simple Installation",
        description='The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured\nfor and sent to a GitHub App. For more information,\nsee "[Using webhooks with GitHub Apps](https://docs.github.com/enterprise-cloud@latest//apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps)."',
    )
    organization: Missing[OrganizationSimpleWebhooks] = Field(
        default=UNSET,
        title="Organization Simple",
        description="A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an\norganization, or when the event occurs from activity in a repository owned by an organization.",
    )
    repository: RepositoryWebhooks = Field(
        title="Repository",
        description="The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property\nwhen the event occurs from activity in a repository.",
    )
    rule: WebhookBranchProtectionRuleDeletedPropRule = Field(
        title="branch protection rule",
        description="The branch protection rule. Includes a `name` and all the [branch protection settings](https://docs.github.com/enterprise-cloud@latest//github/administering-a-repository/defining-the-mergeability-of-pull-requests/about-protected-branches#about-branch-protection-settings) applied to branches that match the name. Binary settings are boolean. Multi-level configurations are one of `off`, `non_admins`, or `everyone`. Actor and build lists are arrays of strings.",
    )
    sender: SimpleUserWebhooks = Field(
        title="Simple User",
        description="The GitHub user that triggered the event. This property is included in every webhook payload.",
    )


class WebhookBranchProtectionRuleDeletedPropRule(GitHubModel):
    """branch protection rule

    The branch protection rule. Includes a `name` and all the [branch protection
    settings](https://docs.github.com/enterprise-cloud@latest//github/administering-
    a-repository/defining-the-mergeability-of-pull-requests/about-protected-
    branches#about-branch-protection-settings) applied to branches that match the
    name. Binary settings are boolean. Multi-level configurations are one of `off`,
    `non_admins`, or `everyone`. Actor and build lists are arrays of strings.
    """

    admin_enforced: bool = Field()
    allow_deletions_enforcement_level: Literal[
        "off", "non_admins", "everyone"
    ] = Field()
    allow_force_pushes_enforcement_level: Literal[
        "off", "non_admins", "everyone"
    ] = Field()
    authorized_actor_names: List[str] = Field()
    authorized_actors_only: bool = Field()
    authorized_dismissal_actors_only: bool = Field()
    create_protected: Missing[bool] = Field(default=UNSET)
    created_at: datetime = Field()
    dismiss_stale_reviews_on_push: bool = Field()
    id: int = Field()
    ignore_approvals_from_contributors: bool = Field()
    linear_history_requirement_enforcement_level: Literal[
        "off", "non_admins", "everyone"
    ] = Field()
    merge_queue_enforcement_level: Literal["off", "non_admins", "everyone"] = Field()
    name: str = Field()
    pull_request_reviews_enforcement_level: Literal[
        "off", "non_admins", "everyone"
    ] = Field()
    repository_id: int = Field()
    require_code_owner_review: bool = Field()
    require_last_push_approval: Missing[bool] = Field(
        default=UNSET,
        description="Whether the most recent push must be approved by someone other than the person who pushed it",
    )
    required_approving_review_count: int = Field()
    required_conversation_resolution_level: Literal[
        "off", "non_admins", "everyone"
    ] = Field()
    required_deployments_enforcement_level: Literal[
        "off", "non_admins", "everyone"
    ] = Field()
    required_status_checks: List[str] = Field()
    required_status_checks_enforcement_level: Literal[
        "off", "non_admins", "everyone"
    ] = Field()
    signature_requirement_enforcement_level: Literal[
        "off", "non_admins", "everyone"
    ] = Field()
    strict_required_status_checks_policy: bool = Field()
    updated_at: datetime = Field()


model_rebuild(WebhookBranchProtectionRuleDeleted)
model_rebuild(WebhookBranchProtectionRuleDeletedPropRule)

__all__ = (
    "WebhookBranchProtectionRuleDeleted",
    "WebhookBranchProtectionRuleDeletedPropRule",
)
