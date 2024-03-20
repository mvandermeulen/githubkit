"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import List, Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild

from .group_0168 import Deployment
from .group_0289 import PullRequest
from .group_0358 import SimpleInstallation
from .group_0360 import RepositoryWebhooks
from .group_0361 import SimpleUserWebhooks
from .group_0359 import OrganizationSimpleWebhooks


class WebhookDeploymentProtectionRuleRequested(GitHubModel):
    """deployment protection rule requested event"""

    action: Literal["requested"] = Field()
    environment: Missing[str] = Field(
        default=UNSET,
        description="The name of the environment that has the deployment protection rule.",
    )
    event: Missing[str] = Field(
        default=UNSET,
        description="The event that triggered the deployment protection rule.",
    )
    deployment_callback_url: Missing[str] = Field(
        default=UNSET, description="The URL to review the deployment protection rule."
    )
    deployment: Missing[Deployment] = Field(
        default=UNSET,
        title="Deployment",
        description="A request for a specific ref(branch,sha,tag) to be deployed",
    )
    pull_requests: Missing[List[PullRequest]] = Field(default=UNSET)
    repository: Missing[RepositoryWebhooks] = Field(
        default=UNSET,
        title="Repository",
        description="The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property\nwhen the event occurs from activity in a repository.",
    )
    organization: Missing[OrganizationSimpleWebhooks] = Field(
        default=UNSET,
        title="Organization Simple",
        description="A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an\norganization, or when the event occurs from activity in a repository owned by an organization.",
    )
    installation: Missing[SimpleInstallation] = Field(
        default=UNSET,
        title="Simple Installation",
        description='The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured\nfor and sent to a GitHub App. For more information,\nsee "[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps)."',
    )
    sender: Missing[SimpleUserWebhooks] = Field(
        default=UNSET,
        title="Simple User",
        description="The GitHub user that triggered the event. This property is included in every webhook payload.",
    )


model_rebuild(WebhookDeploymentProtectionRuleRequested)

__all__ = ("WebhookDeploymentProtectionRuleRequested",)
