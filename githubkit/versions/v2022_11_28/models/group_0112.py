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

from .group_0113 import RepositoryRuleRequiredDeploymentsPropParameters


class RepositoryRuleRequiredDeployments(GitHubModel):
    """required_deployments

    Choose which environments must be successfully deployed to before refs can be
    pushed into a ref that matches this rule.
    """

    type: Literal["required_deployments"] = Field()
    parameters: Missing[RepositoryRuleRequiredDeploymentsPropParameters] = Field(
        default=UNSET
    )


model_rebuild(RepositoryRuleRequiredDeployments)

__all__ = ("RepositoryRuleRequiredDeployments",)
