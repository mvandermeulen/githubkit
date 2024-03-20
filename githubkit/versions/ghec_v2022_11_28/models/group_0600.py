"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild

from .group_0602 import (
    WebhookMarketplacePurchasePendingChangeCancelledPropMarketplacePurchaseAllof0PropPlan,
    WebhookMarketplacePurchasePendingChangeCancelledPropMarketplacePurchaseAllof0PropAccount,
)


class WebhookMarketplacePurchasePendingChangeCancelledPropMarketplacePurchase(
    GitHubModel
):
    """WebhookMarketplacePurchasePendingChangeCancelledPropMarketplacePurchase"""

    account: WebhookMarketplacePurchasePendingChangeCancelledPropMarketplacePurchaseAllof0PropAccount = Field()
    billing_cycle: str = Field()
    free_trial_ends_on: None = Field()
    next_billing_date: str = Field()
    on_free_trial: bool = Field()
    plan: WebhookMarketplacePurchasePendingChangeCancelledPropMarketplacePurchaseAllof0PropPlan = Field()
    unit_count: int = Field()


model_rebuild(WebhookMarketplacePurchasePendingChangeCancelledPropMarketplacePurchase)

__all__ = ("WebhookMarketplacePurchasePendingChangeCancelledPropMarketplacePurchase",)
