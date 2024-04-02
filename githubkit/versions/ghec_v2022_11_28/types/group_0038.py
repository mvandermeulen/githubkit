"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import TypedDict, NotRequired


class AnnouncementType(TypedDict):
    """Enterprise Announcement

    Enterprise global announcement
    """

    announcement: Union[str, None]
    expires_at: NotRequired[Union[datetime, None]]


__all__ = ("AnnouncementType",)