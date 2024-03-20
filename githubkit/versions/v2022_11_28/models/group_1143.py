"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild


class UserSshSigningKeysPostBody(GitHubModel):
    """UserSshSigningKeysPostBody"""

    title: Missing[str] = Field(
        default=UNSET, description="A descriptive name for the new key."
    )
    key: str = Field(
        pattern="^ssh-(rsa|dss|ed25519) |^ecdsa-sha2-nistp(256|384|521) |^(sk-ssh-ed25519|sk-ecdsa-sha2-nistp256)@openssh.com ",
        description='The public SSH key to add to your GitHub account. For more information, see "[Checking for existing SSH keys](https://docs.github.com/authentication/connecting-to-github-with-ssh/checking-for-existing-ssh-keys)."',
    )


model_rebuild(UserSshSigningKeysPostBody)

__all__ = ("UserSshSigningKeysPostBody",)
