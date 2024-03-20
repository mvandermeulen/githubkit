"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing_extensions import TypedDict, NotRequired


class RunnerApplicationType(TypedDict):
    """Runner Application

    Runner Application
    """

    os: str
    architecture: str
    download_url: str
    filename: str
    temp_download_token: NotRequired[str]
    sha256_checksum: NotRequired[str]


__all__ = ("RunnerApplicationType",)
