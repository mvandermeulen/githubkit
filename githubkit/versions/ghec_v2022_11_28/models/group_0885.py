"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import List

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild

from .group_0017 import Repository


class InstallationRepositoriesGetResponse200(GitHubModel):
    """InstallationRepositoriesGetResponse200"""

    total_count: int = Field()
    repositories: List[Repository] = Field()
    repository_selection: Missing[str] = Field(default=UNSET)


model_rebuild(InstallationRepositoriesGetResponse200)

__all__ = ("InstallationRepositoriesGetResponse200",)
