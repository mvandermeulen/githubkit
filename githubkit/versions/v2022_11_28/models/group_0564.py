"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild


class WebhookMarketplacePurchasePendingChangeCancelledPropMarketplacePurchaseAllof1(
    GitHubModel
):
    """WebhookMarketplacePurchasePendingChangeCancelledPropMarketplacePurchaseAllof1"""

    next_billing_date: str = Field()


model_rebuild(
    WebhookMarketplacePurchasePendingChangeCancelledPropMarketplacePurchaseAllof1
)

__all__ = (
    "WebhookMarketplacePurchasePendingChangeCancelledPropMarketplacePurchaseAllof1",
)