"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild


class PagesDeploymentStatus(GitHubModel):
    """GitHub Pages deployment status"""

    status: Missing[
        Literal[
            "deployment_in_progress",
            "syncing_files",
            "finished_file_sync",
            "updating_pages",
            "purging_cdn",
            "deployment_cancelled",
            "deployment_failed",
            "deployment_content_failed",
            "deployment_attempt_error",
            "deployment_lost",
            "succeed",
        ]
    ] = Field(default=UNSET, description="The current status of the deployment.")


model_rebuild(PagesDeploymentStatus)

__all__ = ("PagesDeploymentStatus",)
