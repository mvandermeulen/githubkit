"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild


class WebhookConfig(GitHubModel):
    """Webhook Configuration

    Configuration object of the webhook
    """

    url: Missing[str] = Field(
        default=UNSET, description="The URL to which the payloads will be delivered."
    )
    content_type: Missing[str] = Field(
        default=UNSET,
        description="The media type used to serialize the payloads. Supported values include `json` and `form`. The default is `form`.",
    )
    secret: Missing[str] = Field(
        default=UNSET,
        description="If provided, the `secret` will be used as the `key` to generate the HMAC hex digest value for [delivery signature headers](https://docs.github.com/enterprise-cloud@latest//webhooks/event-payloads/#delivery-headers).",
    )
    insecure_ssl: Missing[Union[str, float]] = Field(default=UNSET)


model_rebuild(WebhookConfig)

__all__ = ("WebhookConfig",)