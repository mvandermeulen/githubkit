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


class ProjectsProjectIdPatchResponse403(GitHubModel):
    """ProjectsProjectIdPatchResponse403"""

    message: Missing[str] = Field(default=UNSET)
    documentation_url: Missing[str] = Field(default=UNSET)
    errors: Missing[List[str]] = Field(default=UNSET)


model_rebuild(ProjectsProjectIdPatchResponse403)

__all__ = ("ProjectsProjectIdPatchResponse403",)
