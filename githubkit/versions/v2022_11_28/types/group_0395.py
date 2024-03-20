"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import Literal
from typing_extensions import TypedDict, NotRequired

from .group_0357 import EnterpriseWebhooksType
from .group_0358 import SimpleInstallationType
from .group_0361 import SimpleUserWebhooksType
from .group_0359 import OrganizationSimpleWebhooksType


class WebhookCustomPropertyDeletedType(TypedDict):
    """custom property deleted event"""

    action: Literal["deleted"]
    definition: WebhookCustomPropertyDeletedPropDefinitionType
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: OrganizationSimpleWebhooksType
    sender: NotRequired[SimpleUserWebhooksType]


class WebhookCustomPropertyDeletedPropDefinitionType(TypedDict):
    """WebhookCustomPropertyDeletedPropDefinition"""

    property_name: str


__all__ = (
    "WebhookCustomPropertyDeletedType",
    "WebhookCustomPropertyDeletedPropDefinitionType",
)
