"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing_extensions import TypedDict


class DependabotPublicKeyType(TypedDict):
    """DependabotPublicKey

    The public key used for setting Dependabot Secrets.
    """

    key_id: str
    key: str


__all__ = ("DependabotPublicKeyType",)
