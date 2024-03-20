"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild


class ReposOwnerRepoEnvironmentsEnvironmentNameSecretsSecretNamePutBody(GitHubModel):
    """ReposOwnerRepoEnvironmentsEnvironmentNameSecretsSecretNamePutBody"""

    encrypted_value: str = Field(
        pattern="^(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=|[A-Za-z0-9+/]{4})$",
        description="Value for your secret, encrypted with [LibSodium](https://libsodium.gitbook.io/doc/bindings_for_other_languages) using the public key retrieved from the [Get an environment public key](https://docs.github.com/rest/actions/secrets#get-an-environment-public-key) endpoint.",
    )
    key_id: str = Field(description="ID of the key you used to encrypt the secret.")


model_rebuild(ReposOwnerRepoEnvironmentsEnvironmentNameSecretsSecretNamePutBody)

__all__ = ("ReposOwnerRepoEnvironmentsEnvironmentNameSecretsSecretNamePutBody",)
