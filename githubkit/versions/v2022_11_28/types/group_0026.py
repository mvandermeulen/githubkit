"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import Union, Literal
from typing_extensions import TypedDict

from .group_0025 import DependabotAlertPackageType


class DependabotAlertSecurityVulnerabilityType(TypedDict):
    """DependabotAlertSecurityVulnerability

    Details pertaining to one vulnerable version range for the advisory.
    """

    package: DependabotAlertPackageType
    severity: Literal["low", "medium", "high", "critical"]
    vulnerable_version_range: str
    first_patched_version: Union[
        DependabotAlertSecurityVulnerabilityPropFirstPatchedVersionType, None
    ]


class DependabotAlertSecurityVulnerabilityPropFirstPatchedVersionType(TypedDict):
    """DependabotAlertSecurityVulnerabilityPropFirstPatchedVersion

    Details pertaining to the package version that patches this vulnerability.
    """

    identifier: str


__all__ = (
    "DependabotAlertSecurityVulnerabilityType",
    "DependabotAlertSecurityVulnerabilityPropFirstPatchedVersionType",
)
