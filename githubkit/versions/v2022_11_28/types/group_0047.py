"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import Union
from typing_extensions import TypedDict, NotRequired

from .group_0045 import MarketplaceListingPlanType


class MarketplacePurchasePropMarketplacePendingChangeType(TypedDict):
    """MarketplacePurchasePropMarketplacePendingChange"""

    is_installed: NotRequired[bool]
    effective_date: NotRequired[str]
    unit_count: NotRequired[Union[int, None]]
    id: NotRequired[int]
    plan: NotRequired[MarketplaceListingPlanType]


class MarketplacePurchasePropMarketplacePurchaseType(TypedDict):
    """MarketplacePurchasePropMarketplacePurchase"""

    billing_cycle: NotRequired[str]
    next_billing_date: NotRequired[Union[str, None]]
    is_installed: NotRequired[bool]
    unit_count: NotRequired[Union[int, None]]
    on_free_trial: NotRequired[bool]
    free_trial_ends_on: NotRequired[Union[str, None]]
    updated_at: NotRequired[str]
    plan: NotRequired[MarketplaceListingPlanType]


__all__ = (
    "MarketplacePurchasePropMarketplacePendingChangeType",
    "MarketplacePurchasePropMarketplacePurchaseType",
)
