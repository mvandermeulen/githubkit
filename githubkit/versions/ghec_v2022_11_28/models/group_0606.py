"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import List, Union, Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild


class WebhookMarketplacePurchasePurchasedPropMarketplacePurchaseAllof1(GitHubModel):
    """WebhookMarketplacePurchasePurchasedPropMarketplacePurchaseAllof1"""

    account: Missing[
        WebhookMarketplacePurchasePurchasedPropMarketplacePurchaseAllof1PropAccount
    ] = Field(default=UNSET)
    billing_cycle: Missing[str] = Field(default=UNSET)
    free_trial_ends_on: Missing[Union[str, None]] = Field(default=UNSET)
    next_billing_date: Union[str, None] = Field()
    on_free_trial: Missing[bool] = Field(default=UNSET)
    plan: Missing[
        WebhookMarketplacePurchasePurchasedPropMarketplacePurchaseAllof1PropPlan
    ] = Field(default=UNSET)
    unit_count: Missing[int] = Field(default=UNSET)


class WebhookMarketplacePurchasePurchasedPropMarketplacePurchaseAllof1PropAccount(
    GitHubModel
):
    """WebhookMarketplacePurchasePurchasedPropMarketplacePurchaseAllof1PropAccount"""

    id: Missing[int] = Field(default=UNSET)
    login: Missing[str] = Field(default=UNSET)
    node_id: Missing[str] = Field(default=UNSET)
    organization_billing_email: Missing[Union[str, None]] = Field(default=UNSET)
    type: Missing[str] = Field(default=UNSET)


class WebhookMarketplacePurchasePurchasedPropMarketplacePurchaseAllof1PropPlan(
    GitHubModel
):
    """WebhookMarketplacePurchasePurchasedPropMarketplacePurchaseAllof1PropPlan"""

    bullets: Missing[List[Union[str, None]]] = Field(default=UNSET)
    description: Missing[str] = Field(default=UNSET)
    has_free_trial: Missing[bool] = Field(default=UNSET)
    id: Missing[int] = Field(default=UNSET)
    monthly_price_in_cents: Missing[int] = Field(default=UNSET)
    name: Missing[str] = Field(default=UNSET)
    price_model: Missing[Literal["FREE", "FLAT_RATE", "PER_UNIT"]] = Field(
        default=UNSET
    )
    unit_name: Missing[Union[str, None]] = Field(default=UNSET)
    yearly_price_in_cents: Missing[int] = Field(default=UNSET)


model_rebuild(WebhookMarketplacePurchasePurchasedPropMarketplacePurchaseAllof1)
model_rebuild(
    WebhookMarketplacePurchasePurchasedPropMarketplacePurchaseAllof1PropAccount
)
model_rebuild(WebhookMarketplacePurchasePurchasedPropMarketplacePurchaseAllof1PropPlan)

__all__ = (
    "WebhookMarketplacePurchasePurchasedPropMarketplacePurchaseAllof1",
    "WebhookMarketplacePurchasePurchasedPropMarketplacePurchaseAllof1PropAccount",
    "WebhookMarketplacePurchasePurchasedPropMarketplacePurchaseAllof1PropPlan",
)
