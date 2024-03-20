"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import List, Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0390 import EnterpriseWebhooksType
from .group_0391 import SimpleInstallationType
from .group_0393 import RepositoryWebhooksType
from .group_0394 import SimpleUserWebhooksType
from .group_0392 import OrganizationSimpleWebhooksType


class WebhookMarketplacePurchaseCancelledType(TypedDict):
    """marketplace_purchase cancelled event"""

    action: Literal["cancelled"]
    effective_date: str
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    marketplace_purchase: WebhookMarketplacePurchaseCancelledPropMarketplacePurchaseType
    organization: NotRequired[OrganizationSimpleWebhooksType]
    previous_marketplace_purchase: NotRequired[
        WebhookMarketplacePurchaseCancelledPropPreviousMarketplacePurchaseType
    ]
    repository: NotRequired[RepositoryWebhooksType]
    sender: SimpleUserWebhooksType


class WebhookMarketplacePurchaseCancelledPropMarketplacePurchaseType(TypedDict):
    """WebhookMarketplacePurchaseCancelledPropMarketplacePurchase"""

    account: WebhookMarketplacePurchaseCancelledPropMarketplacePurchaseMergedAccountType
    billing_cycle: str
    free_trial_ends_on: Union[Union[str, None], None]
    next_billing_date: Union[Union[str, None], None]
    on_free_trial: bool
    plan: WebhookMarketplacePurchaseCancelledPropMarketplacePurchaseMergedPlanType
    unit_count: int


class WebhookMarketplacePurchaseCancelledPropMarketplacePurchaseMergedAccountType(
    TypedDict
):
    """WebhookMarketplacePurchaseCancelledPropMarketplacePurchaseMergedAccount"""

    id: int
    login: str
    node_id: str
    organization_billing_email: Union[Union[str, None], None]
    type: str


class WebhookMarketplacePurchaseCancelledPropMarketplacePurchaseMergedPlanType(
    TypedDict
):
    """WebhookMarketplacePurchaseCancelledPropMarketplacePurchaseMergedPlan"""

    bullets: List[str]
    description: str
    has_free_trial: bool
    id: int
    monthly_price_in_cents: int
    name: str
    price_model: Literal["FREE", "FLAT_RATE", "PER_UNIT"]
    unit_name: Union[Union[str, None], None]
    yearly_price_in_cents: int


class WebhookMarketplacePurchaseCancelledPropPreviousMarketplacePurchaseType(TypedDict):
    """Marketplace Purchase"""

    account: WebhookMarketplacePurchaseCancelledPropPreviousMarketplacePurchasePropAccountType
    billing_cycle: str
    free_trial_ends_on: None
    next_billing_date: NotRequired[Union[str, None]]
    on_free_trial: bool
    plan: WebhookMarketplacePurchaseCancelledPropPreviousMarketplacePurchasePropPlanType
    unit_count: int


class WebhookMarketplacePurchaseCancelledPropPreviousMarketplacePurchasePropAccountType(
    TypedDict
):
    """WebhookMarketplacePurchaseCancelledPropPreviousMarketplacePurchasePropAccount"""

    id: int
    login: str
    node_id: str
    organization_billing_email: Union[str, None]
    type: str


class WebhookMarketplacePurchaseCancelledPropPreviousMarketplacePurchasePropPlanType(
    TypedDict
):
    """WebhookMarketplacePurchaseCancelledPropPreviousMarketplacePurchasePropPlan"""

    bullets: List[str]
    description: str
    has_free_trial: bool
    id: int
    monthly_price_in_cents: int
    name: str
    price_model: Literal["FREE", "FLAT_RATE", "PER_UNIT"]
    unit_name: Union[str, None]
    yearly_price_in_cents: int


__all__ = (
    "WebhookMarketplacePurchaseCancelledType",
    "WebhookMarketplacePurchaseCancelledPropMarketplacePurchaseType",
    "WebhookMarketplacePurchaseCancelledPropMarketplacePurchaseMergedAccountType",
    "WebhookMarketplacePurchaseCancelledPropMarketplacePurchaseMergedPlanType",
    "WebhookMarketplacePurchaseCancelledPropPreviousMarketplacePurchaseType",
    "WebhookMarketplacePurchaseCancelledPropPreviousMarketplacePurchasePropAccountType",
    "WebhookMarketplacePurchaseCancelledPropPreviousMarketplacePurchasePropPlanType",
)
