"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from datetime import datetime
from typing import Any, List, Union

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild


class GpgKey(GitHubModel):
    """GPG Key

    A unique encryption key
    """

    id: int = Field()
    name: Missing[Union[str, None]] = Field(default=UNSET)
    primary_key_id: Union[int, None] = Field()
    key_id: str = Field()
    public_key: str = Field()
    emails: List[GpgKeyPropEmailsItems] = Field()
    subkeys: List[GpgKeyPropSubkeysItems] = Field()
    can_sign: bool = Field()
    can_encrypt_comms: bool = Field()
    can_encrypt_storage: bool = Field()
    can_certify: bool = Field()
    created_at: datetime = Field()
    expires_at: Union[datetime, None] = Field()
    revoked: bool = Field()
    raw_key: Union[str, None] = Field()


class GpgKeyPropEmailsItems(GitHubModel):
    """GpgKeyPropEmailsItems"""

    email: Missing[str] = Field(default=UNSET)
    verified: Missing[bool] = Field(default=UNSET)


class GpgKeyPropSubkeysItems(GitHubModel):
    """GpgKeyPropSubkeysItems"""

    id: Missing[int] = Field(default=UNSET)
    primary_key_id: Missing[int] = Field(default=UNSET)
    key_id: Missing[str] = Field(default=UNSET)
    public_key: Missing[str] = Field(default=UNSET)
    emails: Missing[List[GpgKeyPropSubkeysItemsPropEmailsItems]] = Field(default=UNSET)
    subkeys: Missing[List[Any]] = Field(default=UNSET)
    can_sign: Missing[bool] = Field(default=UNSET)
    can_encrypt_comms: Missing[bool] = Field(default=UNSET)
    can_encrypt_storage: Missing[bool] = Field(default=UNSET)
    can_certify: Missing[bool] = Field(default=UNSET)
    created_at: Missing[str] = Field(default=UNSET)
    expires_at: Missing[Union[str, None]] = Field(default=UNSET)
    raw_key: Missing[Union[str, None]] = Field(default=UNSET)
    revoked: Missing[bool] = Field(default=UNSET)


class GpgKeyPropSubkeysItemsPropEmailsItems(GitHubModel):
    """GpgKeyPropSubkeysItemsPropEmailsItems"""

    email: Missing[str] = Field(default=UNSET)
    verified: Missing[bool] = Field(default=UNSET)


model_rebuild(GpgKey)
model_rebuild(GpgKeyPropEmailsItems)
model_rebuild(GpgKeyPropSubkeysItems)
model_rebuild(GpgKeyPropSubkeysItemsPropEmailsItems)

__all__ = (
    "GpgKey",
    "GpgKeyPropEmailsItems",
    "GpgKeyPropSubkeysItems",
    "GpgKeyPropSubkeysItemsPropEmailsItems",
)
