"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing_extensions import TypedDict


class CombinedBillingUsageType(TypedDict):
    """CombinedBillingUsage"""

    days_left_in_billing_cycle: int
    estimated_paid_storage_for_month: int
    estimated_storage_for_month: int


__all__ = ("CombinedBillingUsageType",)
